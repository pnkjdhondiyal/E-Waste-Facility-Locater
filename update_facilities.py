import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import Facility

# Clear all existing facilities
print("Removing old facilities...")
Facility.objects.all().delete()
print("All old facilities removed.\n")

# Real Certified E-Waste Centers in India
centers = [
    {
        'name': 'Attero Recycling Pvt Ltd',
        'address': 'Raipur Industrial Area, Bhagwanpur, Roorkee, Uttarakhand 247661',
        'latitude': 29.8547,
        'longitude': 77.8888,
        'phone': '+91-120-4318500',
        'email': 'info@attero.in'
    },
    {
        'name': 'E-Parisaraa Pvt Ltd',
        'address': 'No 30 P3 KIADB Industrial Area, Dobaspet, Bangalore Rural, Karnataka 562111',
        'latitude': 13.2379,
        'longitude': 77.1757,
        'phone': '+91-9980147680',
        'email': 'info@eparisaraa.com'
    },
    {
        'name': 'Eco Recycling Ltd (Ecoreco)',
        'address': 'Eco House, MIDC Industrial Area, Andheri East, Mumbai, Maharashtra 400069',
        'latitude': 19.1136,
        'longitude': 72.8697,
        'phone': '+91-22-40052900',
        'email': 'info@ecoreco.com'
    },
    {
        'name': 'E-Waste Recyclers India Pvt Ltd',
        'address': 'UPSIDC Industrial Area, Kosi Kotwan, Mathura, Uttar Pradesh 281403',
        'latitude': 27.7955,
        'longitude': 77.4413,
        'phone': '+91-9412277500',
        'email': 'info@ewri.in'
    },
    {
        'name': 'ETCO E-Waste Recycler Pvt Ltd',
        'address': 'SB-23 Shilp Bari, Road No 14-15, VKI Industrial Area, Jaipur, Rajasthan 302013',
        'latitude': 26.9855,
        'longitude': 75.7911,
        'phone': '+91-9829018257',
        'email': 'etcoewaste@gmail.com'
    },
    {
        'name': 'Cerebra Integrated Technologies Ltd',
        'address': 'Electronics City Phase 1, Bengaluru, Karnataka 560100',
        'latitude': 12.8399,
        'longitude': 77.6770,
        'phone': '+91-80-42485000',
        'email': 'info@cerebracomputers.com'
    },
    {
        'name': 'Greenscape Eco Management Pvt Ltd',
        'address': 'Patparganj Industrial Area, Delhi 110092',
        'latitude': 28.6267,
        'longitude': 77.2925,
        'phone': '+91-11-22158000',
        'email': 'info@greenscapeeco.com'
    },
    {
        'name': 'Techchef E-Waste Solutions Pvt Ltd',
        'address': 'Okhla Industrial Area Phase 2, New Delhi 110020',
        'latitude': 28.5355,
        'longitude': 77.2713,
        'phone': '+91-11-45675300',
        'email': 'info@techchef.in'
    },
    {
        'name': 'Exigo Recycling Pvt Ltd',
        'address': 'Barsat Road Industrial Area, Panipat, Haryana 132103',
        'latitude': 29.3909,
        'longitude': 76.9635,
        'phone': '+91-9992000212',
        'email': 'info@exigorecycling.com'
    },
    {
        'name': 'Green India E-Waste & Recycling OPC Pvt Ltd',
        'address': 'Survey No 74 Hissa 1 Dahisar East, Mumbai, Maharashtra',
        'latitude': 19.2480,
        'longitude': 72.8567,
        'phone': '+91-9820000000',
        'email': 'info@greenindiaewaste.com'
    },
]

# Add all centers
print("Adding Real Certified E-Waste Centers...")
for center in centers:
    Facility.objects.create(**center)
    print(f"[+] Added: {center['name']}")

print(f"\n[OK] Total facilities in database: {Facility.objects.count()}")
print("\nRefresh the map page - centers will be sorted by distance from your location!")
