from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Facility, RecyclingLog, UserProfile
import json

def home(request):
    return render(request, 'core/home.html')

def map_view(request):
    facilities = Facility.objects.all()
    return render(request, 'core/map.html', {'facilities': facilities})

def get_facilities_json(request):
    facilities = list(Facility.objects.values('name', 'address', 'latitude', 'longitude', 'phone', 'email'))
    return JsonResponse(facilities, safe=False)

@csrf_exempt
def calculator(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            brand = data.get('brand')
            processor = data.get('processor')
            gpu = data.get('gpu')
            age = int(data.get('age', 0))
            weight = float(data.get('weight', 0))
            material = data.get('material')
            
            # Base value calculation
            base_values = {
                'Apple': 800, 'Dell': 500, 'HP': 450, 'Lenovo': 480, 'Samsung': 520, 'Other': 300
            }
            processor_multiplier = {
                'i3': 0.6, 'i5': 0.8, 'i7': 1.0, 'i9': 1.3,
                'Ryzen3': 0.65, 'Ryzen5': 0.85, 'Ryzen7': 1.05,
                'M1': 1.2, 'M2': 1.4
            }
            gpu_bonus = {
                'Integrated': 0, 'GTX1650': 100, 'GTX1660': 120,
                'RTX3050': 150, 'RTX3060': 200, 'RTX4060': 250
            }
            
            base = base_values.get(brand, 300)
            proc_mult = processor_multiplier.get(processor, 0.7)
            gpu_add = gpu_bonus.get(gpu, 0)
            
            depreciation = max(0.3, 1 - (age * 0.15))
            estimated_value = (base * proc_mult + gpu_add) * depreciation
            
            # Carbon savings calculation (kg CO2)
            material_factor = {'Plastic': 2.5, 'Aluminum': 8.0, 'Mixed': 5.0}
            manufacturing_co2 = 200
            recycling_benefit = weight * material_factor.get(material, 3.0)
            carbon_saved = manufacturing_co2 + recycling_benefit
            
            # Save log with user if authenticated
            user = request.user if request.user.is_authenticated else None
            RecyclingLog.objects.create(
                user=user,
                device_brand=brand,
                device_processor=processor,
                estimated_value=estimated_value,
                carbon_saved=carbon_saved
            )
            
            # Update user profile if logged in
            if user:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.total_devices_recycled += 1
                profile.total_value_earned += estimated_value
                profile.total_carbon_saved += carbon_saved
                profile.save()
            
            return JsonResponse({
                'estimated_value': round(estimated_value, 2),
                'carbon_saved': round(carbon_saved, 2)
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
