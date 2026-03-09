"""
Template for adding more device prices to the database.
Copy this file and modify the devices list with your own data.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import DevicePrice

# Add your custom devices here
custom_devices = [
    # Template - Copy and modify this structure
    {
        'brand': 'Apple',  # Apple, Dell, HP, Lenovo, Samsung, Other
        'model_name': 'MacBook Pro 16 M1 Pro',
        'processor': 'M1',  # i3, i5, i7, i9, Ryzen3, Ryzen5, Ryzen7, M1, M2
        'gpu': 'Integrated',  # Integrated, GTX1650, GTX1660, RTX3050, RTX3060, RTX4060
        'ram_gb': 16,
        'storage_gb': 512,
        'pristine_price': 1800,  # Like new condition
        'mint_price': 1550,      # Good condition
        'overused_price': 1150,  # Heavy wear
        'release_year': 2021
    },
    
    # Add more devices below (copy the structure above)
    {
        'brand': 'Dell',
        'model_name': 'Alienware m15 R6',
        'processor': 'i9',
        'gpu': 'RTX3060',
        'ram_gb': 32,
        'storage_gb': 1024,
        'pristine_price': 1500,
        'mint_price': 1250,
        'overused_price': 900,
        'release_year': 2021
    },
    
    {
        'brand': 'HP',
        'model_name': 'Spectre x360',
        'processor': 'i7',
        'gpu': 'Integrated',
        'ram_gb': 16,
        'storage_gb': 512,
        'pristine_price': 1000,
        'mint_price': 850,
        'overused_price': 620,
        'release_year': 2022
    },
]

# Create device price entries
for device in custom_devices:
    # Check if device already exists
    existing = DevicePrice.objects.filter(
        brand=device['brand'],
        model_name=device['model_name']
    ).first()
    
    if existing:
        print(f"Skipped (already exists): {device['brand']} {device['model_name']}")
    else:
        DevicePrice.objects.create(**device)
        print(f"Added: {device['brand']} {device['model_name']}")

print(f"\nDone! Check admin panel to verify.")
