from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Facility, RecyclingLog
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
            # Manufacturing new device emissions + Material recycling benefit
            material_factor = {'Plastic': 2.5, 'Aluminum': 8.0, 'Mixed': 5.0}
            manufacturing_co2 = 200  # Average kg CO2 for new device
            recycling_benefit = weight * material_factor.get(material, 3.0)
            carbon_saved = manufacturing_co2 + recycling_benefit
            
            # Save log
            RecyclingLog.objects.create(
                device_brand=brand,
                device_processor=processor,
                estimated_value=estimated_value,
                carbon_saved=carbon_saved
            )
            
            return JsonResponse({
                'estimated_value': round(estimated_value, 2),
                'carbon_saved': round(carbon_saved, 2)
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return render(request, 'core/calculator.html')

def info(request):
    return render(request, 'core/info.html')
