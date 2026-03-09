from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Facility, RecyclingLog, UserProfile, DevicePrice
import json
import re
from PIL import Image
import pytesseract

def home(request):
    return render(request, 'core/home.html')

@login_required
def map_view(request):
    facilities = Facility.objects.all()
    return render(request, 'core/map.html', {'facilities': facilities})

def get_facilities_json(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Login required'}, status=401)
    facilities = list(Facility.objects.values('name', 'address', 'latitude', 'longitude', 'phone', 'email'))
    return JsonResponse(facilities, safe=False)

@login_required
@csrf_exempt
def calculator(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            brand = data.get('brand', '').strip()
            model = data.get('model', '').strip()
            processor = data.get('processor', '').strip() or 'Unknown'
            gpu = data.get('gpu', '').strip() or 'Integrated'
            ram = data.get('ram') or 8
            storage = data.get('storage') or 256
            condition = data.get('condition', 'mint')
            working_status = data.get('working_status', 'fully_working')
            age = int(data.get('age', 0))
            
            # Working status multiplier
            working_multiplier = {
                'fully_working': 1.0,
                'minor_issues': 0.85,
                'major_issues': 0.60,
                'not_working': 0.30
            }
            work_mult = working_multiplier.get(working_status, 1.0)
            
            # Try to find device in database
            device_price = DevicePrice.objects.filter(
                brand__iexact=brand,
                processor__iexact=processor,
                gpu__iexact=gpu
            ).first()
            
            if device_price:
                # Use database prices
                condition_prices = {
                    'pristine': device_price.pristine_price,
                    'mint': device_price.mint_price,
                    'overused': device_price.overused_price
                }
                base_value = condition_prices.get(condition, device_price.mint_price)
                
                # Apply age depreciation
                device_age = 2024 - device_price.release_year + age
                depreciation = max(0.2, 1 - (device_age * 0.12))
                estimated_value = base_value * depreciation * work_mult
            else:
                # Fallback calculation based on brand and condition
                base_values = {
                    'apple': 65000, 'dell': 40000, 'hp': 37000, 'lenovo': 39000, 
                    'samsung': 42000, 'asus': 38000, 'acer': 35000, 'msi': 45000
                }
                
                # Processor multiplier (if provided)
                processor_multiplier = {
                    'i3': 0.6, 'i5': 0.8, 'i7': 1.0, 'i9': 1.3,
                    'ryzen3': 0.65, 'ryzen5': 0.85, 'ryzen7': 1.05, 'ryzen9': 1.25,
                    'm1': 1.2, 'm2': 1.4, 'm3': 1.5, 'unknown': 0.75
                }
                
                # GPU bonus (if provided)
                gpu_bonus = {
                    'integrated': 0, 'gtx1650': 8000, 'gtx1660': 10000,
                    'rtx3050': 12000, 'rtx3060': 16000, 'rtx4060': 20000
                }
                
                condition_multiplier = {'pristine': 1.2, 'mint': 1.0, 'overused': 0.7}
                
                base = base_values.get(brand.lower(), 30000)
                proc_mult = processor_multiplier.get(processor.lower(), 0.75)
                gpu_add = gpu_bonus.get(gpu.lower(), 0)
                cond_mult = condition_multiplier.get(condition, 1.0)
                
                depreciation = max(0.3, 1 - (age * 0.15))
                estimated_value = (base * proc_mult + gpu_add) * depreciation * cond_mult * work_mult
            
            # Carbon savings (fixed estimate)
            carbon_saved = 250
            
            # Save log
            user = request.user if request.user.is_authenticated else None
            RecyclingLog.objects.create(
                user=user,
                device_brand=brand,
                device_processor=processor,
                device_condition=condition,
                estimated_value=estimated_value,
                carbon_saved=carbon_saved
            )
            
            # Update user profile
            if user:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.total_devices_recycled += 1
                profile.total_value_earned += estimated_value
                profile.total_carbon_saved += carbon_saved
                profile.save()
            
            return JsonResponse({
                'estimated_value': round(estimated_value, 2),
                'carbon_saved': round(carbon_saved, 2),
                'condition': condition,
                'currency': 'INR'
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return render(request, 'core/calculator.html')

def info(request):
    return render(request, 'core/info.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)
        login(request, user)
        return redirect('dashboard')
    
    return render(request, 'core/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    recent_logs = RecyclingLog.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    context = {
        'profile': profile,
        'recent_logs': recent_logs,
        'username': request.user.username
    }
    return render(request, 'core/dashboard.html', context)

@login_required
@csrf_exempt
def calculator_upload(request):
    if request.method == 'POST':
        try:
            image_file = request.FILES.get('image')
            condition = request.POST.get('condition', 'mint')
            working_status = request.POST.get('working_status', 'fully_working')
            age = int(request.POST.get('age', 0))
            
            # Working status multiplier
            working_multiplier = {
                'fully_working': 1.0,
                'minor_issues': 0.85,
                'major_issues': 0.60,
                'not_working': 0.30
            }
            work_mult = working_multiplier.get(working_status, 1.0)
            
            if not image_file:
                return JsonResponse({'error': 'No image provided'}, status=400)
            
            try:
                # Open and process image
                image = Image.open(image_file)
                
                # Better preprocessing for OCR
                from PIL import ImageEnhance, ImageFilter
                
                # Resize if too small
                if image.width < 800:
                    image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)
                
                # Convert to grayscale
                image = image.convert('L')
                
                # Enhance contrast
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(2.5)
                
                # Enhance sharpness
                enhancer = ImageEnhance.Sharpness(image)
                image = enhancer.enhance(2)
                
                # Apply slight blur to reduce noise
                image = image.filter(ImageFilter.MedianFilter(size=3))
                
                # Extract text using OCR with better config
                custom_config = r'--oem 3 --psm 6'
                text = pytesseract.image_to_string(image, config=custom_config)
            except Exception as ocr_error:
                print(f"OCR Error: {str(ocr_error)}")
                return JsonResponse({'error': f'OCR failed: {str(ocr_error)}. Make sure Tesseract is installed.'}, status=400)
            
            # Debug: Print extracted text
            print("=" * 50)
            print("EXTRACTED TEXT FROM IMAGE:")
            print(text)
            print("=" * 50)
            
            # Extract device specs from text
            specs = extract_specs_from_text(text)
            
            # Debug: Print detected specs
            print("DETECTED SPECS:", specs)
            print("=" * 50)
            
            # Calculate value using extracted specs
            brand = specs.get('brand', 'Unknown')
            processor = specs.get('processor', 'Unknown')
            gpu = specs.get('gpu', 'Integrated')
            ram = specs.get('ram', 8)
            
            # Try database lookup
            device_price = DevicePrice.objects.filter(
                brand__iexact=brand,
                processor__iexact=processor,
                gpu__iexact=gpu
            ).first()
            
            if device_price:
                condition_prices = {
                    'pristine': device_price.pristine_price,
                    'mint': device_price.mint_price,
                    'overused': device_price.overused_price
                }
                base_value = condition_prices.get(condition, device_price.mint_price)
                device_age = 2024 - device_price.release_year + age
                depreciation = max(0.2, 1 - (device_age * 0.12))
                estimated_value = base_value * depreciation * work_mult
            else:
                # Fallback calculation
                base_values = {
                    'apple': 65000, 'dell': 40000, 'hp': 37000, 'lenovo': 39000,
                    'samsung': 42000, 'asus': 38000, 'acer': 35000, 'msi': 45000, 'unknown': 30000
                }
                processor_multiplier = {
                    'i3': 0.6, 'i5': 0.8, 'i7': 1.0, 'i9': 1.3,
                    'ryzen3': 0.65, 'ryzen5': 0.85, 'ryzen7': 1.05,
                    'm1': 1.2, 'm2': 1.4, 'unknown': 0.75
                }
                condition_multiplier = {'pristine': 1.2, 'mint': 1.0, 'overused': 0.7}
                
                base = base_values.get(brand.lower(), 30000)
                proc_mult = processor_multiplier.get(processor.lower(), 0.75)
                cond_mult = condition_multiplier.get(condition, 1.0)
                depreciation = max(0.3, 1 - (age * 0.15))
                estimated_value = base * proc_mult * depreciation * cond_mult * work_mult
            
            carbon_saved = 250
            
            # Save log
            user = request.user if request.user.is_authenticated else None
            RecyclingLog.objects.create(
                user=user,
                device_brand=brand,
                device_processor=processor,
                device_condition=condition,
                estimated_value=estimated_value,
                carbon_saved=carbon_saved
            )
            
            # Update user profile
            if user:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.total_devices_recycled += 1
                profile.total_value_earned += estimated_value
                profile.total_carbon_saved += carbon_saved
                profile.save()
            
            return JsonResponse({
                'estimated_value': round(estimated_value, 2),
                'carbon_saved': round(carbon_saved, 2),
                'condition': condition,
                'currency': 'INR',
                'extracted_specs': specs,
                'extracted_text': text[:500]  # First 500 chars for debugging
            })
            
        except Exception as e:
            print(f"Upload Error: {str(e)}")
            import traceback
            traceback.print_exc()
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def extract_specs_from_text(text):
    """Extract device specifications from OCR text"""
    text_lower = text.lower()
    text_clean = re.sub(r'[^a-z0-9\s:]+', ' ', text_lower)  # Remove special chars
    specs = {}
    
    # Extract brand - more flexible
    brands = ['apple', 'dell', 'hp', 'lenovo', 'samsung', 'asus', 'acer', 'msi', 'microsoft', 'surface']
    for brand in brands:
        if brand in text_lower:
            if brand == 'surface':
                specs['brand'] = 'Microsoft'
            else:
                specs['brand'] = brand.capitalize()
            break
    
    # Extract processor - very flexible patterns
    processor_patterns = [
        r'intel.*?core.*?i[3579]',
        r'core.*?i[3579]',
        r'i[3579][-\s]*\d{4}[a-z]*',
        r'\bi[3579]\b',
        r'ryzen\s*[3579]',
        r'amd.*?ryzen.*?[3579]',
        r'apple\s*m[123]',
        r'm[123]\s*(?:pro|max|ultra)?',
        r'processor.*?i[3579]',
        r'cpu.*?i[3579]',
    ]
    for pattern in processor_patterns:
        match = re.search(pattern, text_lower)
        if match:
            proc = match.group(0).strip()
            if 'i3' in proc: specs['processor'] = 'i3'
            elif 'i5' in proc: specs['processor'] = 'i5'
            elif 'i7' in proc: specs['processor'] = 'i7'
            elif 'i9' in proc: specs['processor'] = 'i9'
            elif 'ryzen' in proc:
                if '3' in proc: specs['processor'] = 'Ryzen3'
                elif '5' in proc: specs['processor'] = 'Ryzen5'
                elif '7' in proc: specs['processor'] = 'Ryzen7'
                elif '9' in proc: specs['processor'] = 'Ryzen9'
            elif 'm1' in proc: specs['processor'] = 'M1'
            elif 'm2' in proc: specs['processor'] = 'M2'
            elif 'm3' in proc: specs['processor'] = 'M3'
            break
    
    # Extract RAM - very flexible patterns
    ram_patterns = [
        r'(\d+\.\d+)\s*gb\s*(?:of\s*)?(?:ram|memory)',  # 8.00 GB RAM
        r'(?:ram|memory)\s*(?::|\s)*\s*(\d+\.\d+)\s*gb',  # RAM 8.00 GB
        r'installed\s*(?:ram|memory)\s*(?::|\s)*\s*(\d+\.\d+)\s*gb',  # Installed RAM 8.00 GB
        r'(\d+)\s*gb\s*(?:of\s*)?(?:ram|memory)',
        r'(?:ram|memory)\s*(?::|\s)*\s*(\d+)\s*gb',
        r'installed\s*(?:ram|memory)\s*(?::|\s)*\s*(\d+)\s*gb',
        r'(\d+)\s*gb\s*(?:ddr|ram)',
        r'(\d+)\s*gb.*?(?:installed|memory|ram)',
        r'memory.*?(\d+)\s*gb',
        r'(\d+)\s*gb\s+ram',
        r'ram\s+(\d+)\s*gb',
        r'(\d+)gb\s*(?:ram|memory)',
        r'(?:ram|memory)\s*(\d+)gb',
        r'(?:ram|memory)[^\d]*(\d+)',
    ]
    for pattern in ram_patterns:
        match = re.search(pattern, text_lower)
        if match:
            try:
                ram_str = match.group(1)
                ram_value = int(float(ram_str))  # Convert 8.00 to 8
                if 2 <= ram_value <= 128:
                    specs['ram'] = ram_value
                    break
            except:
                continue
    
    # Extract Storage - flexible patterns (prioritize total storage over used)
    storage_patterns = [
        r'of\s+(\d+)\s*gb',  # of 477 GB (total storage)
        r'(\d+)\s*gb\s*(?:ssd|hdd|storage|nvme|disk)',
        r'(?:ssd|hdd|storage|nvme|disk)\s*(?::|\s)*\s*(\d+)\s*gb',
        r'(\d+)\s*tb\s*(?:ssd|hdd|storage|nvme|disk)',
        r'(?:ssd|hdd|storage|nvme|disk)\s*(?::|\s)*\s*(\d+)\s*tb',
        r'storage.*?(\d+)\s*(?:gb|tb)',
        r'b\s+storage.*?(\d+)\s*gb',  # B Storage 477 GB
    ]
    for pattern in storage_patterns:
        match = re.search(pattern, text_lower)
        if match:
            try:
                storage_value = int(match.group(1))
                if 'tb' in match.group(0):
                    storage_value *= 1024
                # Valid storage range (exclude RAM values)
                if 64 <= storage_value <= 4096 and storage_value != specs.get('ram', 0):
                    specs['storage'] = storage_value
                    break
            except:
                continue
    
    # Extract GPU - flexible patterns
    gpu_patterns = [
        r'amd\s+radeon.*?vega\s*\d+',  # AMD Radeon Vega 8
        r'radeon.*?vega\s*\d+',  # Radeon Vega 8
        r'vega\s*\d+',  # Vega 8
        r'(?:nvidia\s*)?(?:geforce\s*)?rtx\s*\d{4}',
        r'(?:nvidia\s*)?(?:geforce\s*)?gtx\s*\d{4}',
        r'rtx\s*\d{4}',
        r'gtx\s*\d{4}',
        r'intel.*?(?:uhd|iris|hd).*?graphics',
        r'amd.*?radeon',
        r'integrated.*?graphics',
        r'graphics.*?integrated',
        r'intel.*?graphics',
    ]
    for pattern in gpu_patterns:
        match = re.search(pattern, text_lower)
        if match:
            gpu = match.group(0).strip()
            if 'vega' in gpu:
                vega_model = re.search(r'vega\s*(\d+)', gpu)
                if vega_model:
                    specs['gpu'] = f'Vega{vega_model.group(1)}'
                else:
                    specs['gpu'] = 'Integrated'
            elif 'rtx' in gpu:
                gpu_model = re.search(r'rtx\s*(\d{4})', gpu)
                if gpu_model:
                    specs['gpu'] = f'RTX{gpu_model.group(1)}'
            elif 'gtx' in gpu:
                gpu_model = re.search(r'gtx\s*(\d{4})', gpu)
                if gpu_model:
                    specs['gpu'] = f'GTX{gpu_model.group(1)}'
            else:
                specs['gpu'] = 'Integrated'
            break
    
    # Set defaults if not found
    if 'gpu' not in specs:
        specs['gpu'] = 'Integrated'
    
    return specs
