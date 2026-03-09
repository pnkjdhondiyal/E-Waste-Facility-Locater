import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import DevicePrice

# Clear existing data
DevicePrice.objects.all().delete()

# Real-world device prices based on market data
devices = [
    # Apple MacBooks
    {'brand': 'Apple', 'model_name': 'MacBook Air M1', 'processor': 'M1', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 850, 'mint_price': 750, 'overused_price': 550, 'release_year': 2020},
    {'brand': 'Apple', 'model_name': 'MacBook Air M2', 'processor': 'M2', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 1100, 'mint_price': 950, 'overused_price': 700, 'release_year': 2022},
    {'brand': 'Apple', 'model_name': 'MacBook Pro M1', 'processor': 'M1', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 1300, 'mint_price': 1100, 'overused_price': 850, 'release_year': 2020},
    {'brand': 'Apple', 'model_name': 'MacBook Pro M2', 'processor': 'M2', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 1600, 'mint_price': 1400, 'overused_price': 1050, 'release_year': 2022},
    
    # Dell Laptops
    {'brand': 'Dell', 'model_name': 'Inspiron 15 i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 480, 'mint_price': 400, 'overused_price': 280, 'release_year': 2021},
    {'brand': 'Dell', 'model_name': 'XPS 13 i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 900, 'mint_price': 750, 'overused_price': 550, 'release_year': 2021},
    {'brand': 'Dell', 'model_name': 'G15 Gaming i7 RTX3060', 'processor': 'i7', 'gpu': 'RTX3060', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 1100, 'mint_price': 950, 'overused_price': 700, 'release_year': 2022},
    {'brand': 'Dell', 'model_name': 'Inspiron 14 i3', 'processor': 'i3', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 350, 'mint_price': 280, 'overused_price': 180, 'release_year': 2020},
    
    # HP Laptops
    {'brand': 'HP', 'model_name': 'Pavilion 15 i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 450, 'mint_price': 380, 'overused_price': 260, 'release_year': 2021},
    {'brand': 'HP', 'model_name': 'Envy 13 i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 850, 'mint_price': 700, 'overused_price': 500, 'release_year': 2021},
    {'brand': 'HP', 'model_name': 'Omen 15 i7 RTX3050', 'processor': 'i7', 'gpu': 'RTX3050', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 950, 'mint_price': 800, 'overused_price': 600, 'release_year': 2022},
    {'brand': 'HP', 'model_name': 'Pavilion Gaming i5 GTX1650', 'processor': 'i5', 'gpu': 'GTX1650', 'ram_gb': 8, 'storage_gb': 512, 
     'pristine_price': 650, 'mint_price': 550, 'overused_price': 400, 'release_year': 2020},
    
    # Lenovo Laptops
    {'brand': 'Lenovo', 'model_name': 'IdeaPad 3 i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 460, 'mint_price': 390, 'overused_price': 270, 'release_year': 2021},
    {'brand': 'Lenovo', 'model_name': 'ThinkPad X1 i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 1000, 'mint_price': 850, 'overused_price': 620, 'release_year': 2021},
    {'brand': 'Lenovo', 'model_name': 'Legion 5 Ryzen7 RTX3060', 'processor': 'Ryzen7', 'gpu': 'RTX3060', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 1150, 'mint_price': 980, 'overused_price': 720, 'release_year': 2022},
    {'brand': 'Lenovo', 'model_name': 'IdeaPad Gaming Ryzen5 GTX1650', 'processor': 'Ryzen5', 'gpu': 'GTX1650', 'ram_gb': 8, 'storage_gb': 512, 
     'pristine_price': 620, 'mint_price': 520, 'overused_price': 380, 'release_year': 2021},
    
    # Samsung Laptops
    {'brand': 'Samsung', 'model_name': 'Galaxy Book i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 520, 'mint_price': 440, 'overused_price': 310, 'release_year': 2021},
    {'brand': 'Samsung', 'model_name': 'Galaxy Book Pro i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 880, 'mint_price': 730, 'overused_price': 530, 'release_year': 2021},
    
    # Budget/Other Options
    {'brand': 'Other', 'model_name': 'Generic i3 Laptop', 'processor': 'i3', 'gpu': 'Integrated', 'ram_gb': 4, 'storage_gb': 256, 
     'pristine_price': 280, 'mint_price': 220, 'overused_price': 140, 'release_year': 2020},
    {'brand': 'Other', 'model_name': 'Generic i5 Laptop', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 380, 'mint_price': 310, 'overused_price': 210, 'release_year': 2020},
]

# Create device price entries
for device in devices:
    DevicePrice.objects.create(**device)
    print(f"Added: {device['brand']} {device['model_name']}")

print(f"\n✅ Successfully added {len(devices)} device prices to database!")
print("You can now use the calculator with real market prices.")
