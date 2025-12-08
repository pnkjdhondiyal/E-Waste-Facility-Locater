import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import Facility

# Clear existing facilities
Facility.objects.all().delete()

# Add sample facilities
facilities = [
    {
        'name': 'Green E-Waste Recycling Center',
        'address': 'Connaught Place, New Delhi',
        'latitude': 28.6315,
        'longitude': 77.2167,
        'phone': '+91-11-12345678',
        'email': 'info@greenewaste.com'
    },
    {
        'name': 'EcoTech Recyclers',
        'address': 'Nehru Place, New Delhi',
        'latitude': 28.5494,
        'longitude': 77.2501,
        'phone': '+91-11-98765432',
        'email': 'contact@ecotech.com'
    },
    {
        'name': 'Delhi E-Waste Hub',
        'address': 'Lajpat Nagar, New Delhi',
        'latitude': 28.5677,
        'longitude': 77.2431,
        'phone': '+91-11-55667788',
        'email': 'info@delhiewaste.com'
    },
    {
        'name': 'Recycle India Center',
        'address': 'Karol Bagh, New Delhi',
        'latitude': 28.6519,
        'longitude': 77.1900,
        'phone': '+91-11-44556677',
        'email': 'support@recycleindia.com'
    },
    {
        'name': 'Tech Waste Solutions',
        'address': 'Dwarka, New Delhi',
        'latitude': 28.5921,
        'longitude': 77.0460,
        'phone': '+91-11-33445566',
        'email': 'hello@techwaste.com'
    }
]

for facility_data in facilities:
    Facility.objects.create(**facility_data)
    print(f"Added: {facility_data['name']}")

print(f"\nTotal facilities added: {Facility.objects.count()}")
