import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import Facility

# E-Waste Centers in Delhi
delhi_centers = [
    {
        'name': 'Green E-Waste Recycling Center',
        'address': 'Connaught Place, New Delhi, Delhi 110001',
        'latitude': 28.6315,
        'longitude': 77.2167,
        'phone': '+91-11-23456789',
        'email': 'info@greenewaste.com'
    },
    {
        'name': 'EcoTech Recyclers Delhi',
        'address': 'Nehru Place, New Delhi, Delhi 110019',
        'latitude': 28.5494,
        'longitude': 77.2501,
        'phone': '+91-11-26543210',
        'email': 'contact@ecotech-delhi.com'
    },
    {
        'name': 'Delhi E-Waste Management',
        'address': 'Lajpat Nagar, New Delhi, Delhi 110024',
        'latitude': 28.5677,
        'longitude': 77.2431,
        'phone': '+91-11-29876543',
        'email': 'info@delhiewaste.com'
    },
    {
        'name': 'Capital Recycling Solutions',
        'address': 'Dwarka Sector 10, New Delhi, Delhi 110075',
        'latitude': 28.5921,
        'longitude': 77.0460,
        'phone': '+91-11-25678901',
        'email': 'support@capitalrecycling.com'
    },
    {
        'name': 'Metro E-Waste Center',
        'address': 'Rajouri Garden, New Delhi, Delhi 110027',
        'latitude': 28.6414,
        'longitude': 77.1231,
        'phone': '+91-11-25432109',
        'email': 'metro@ewastecenter.com'
    },
]

# E-Waste Centers in Dehradun
dehradun_centers = [
    {
        'name': 'Himalayan E-Waste Recyclers',
        'address': 'Rajpur Road, Dehradun, Uttarakhand 248001',
        'latitude': 30.3255,
        'longitude': 78.0436,
        'phone': '+91-135-2654321',
        'email': 'info@himalayanewaste.com'
    },
    {
        'name': 'Doon Valley Recycling Center',
        'address': 'Clock Tower, Dehradun, Uttarakhand 248001',
        'latitude': 30.3165,
        'longitude': 78.0322,
        'phone': '+91-135-2789012',
        'email': 'contact@doonvalley.com'
    },
    {
        'name': 'Green Hills E-Waste Management',
        'address': 'Saharanpur Road, Dehradun, Uttarakhand 248001',
        'latitude': 30.3398,
        'longitude': 78.0515,
        'phone': '+91-135-2876543',
        'email': 'greenhills@ewaste.com'
    },
]

# Add Delhi centers
print("Adding Delhi E-Waste Centers...")
for center in delhi_centers:
    facility, created = Facility.objects.get_or_create(
        name=center['name'],
        defaults=center
    )
    if created:
        print(f"[+] Added: {center['name']}")
    else:
        print(f"[-] Already exists: {center['name']}")

# Add Dehradun centers
print("\nAdding Dehradun E-Waste Centers...")
for center in dehradun_centers:
    facility, created = Facility.objects.get_or_create(
        name=center['name'],
        defaults=center
    )
    if created:
        print(f"[+] Added: {center['name']}")
    else:
        print(f"[-] Already exists: {center['name']}")

print(f"\n[OK] Total facilities in database: {Facility.objects.count()}")
print("\nRefresh the map page to see all centers!")
