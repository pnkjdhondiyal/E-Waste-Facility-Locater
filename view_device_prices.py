import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import DevicePrice

print("=" * 70)
print("DEVICE PRICES IN DATABASE")
print("=" * 70)

devices = DevicePrice.objects.all().order_by('brand', '-pristine_price')

if not devices:
    print("\nNo devices found in database!")
    print("Run: python populate_device_prices.py")
else:
    print(f"\nTotal Devices: {devices.count()}\n")
    
    current_brand = None
    for device in devices:
        if current_brand != device.brand:
            current_brand = device.brand
            print(f"\n--- {current_brand} ---")
        
        print(f"\n{device.model_name}")
        print(f"  Specs: {device.processor} | {device.gpu} | {device.ram_gb}GB RAM | {device.storage_gb}GB")
        print(f"  Pristine: ${device.pristine_price} | Mint: ${device.mint_price} | Overused: ${device.overused_price}")
        print(f"  Released: {device.release_year}")

print("\n" + "=" * 70)
print("Use admin panel to add/edit prices: http://127.0.0.1:8000/admin/")
print("=" * 70)
