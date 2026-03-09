import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elocate.settings')
django.setup()

from core.models import DevicePrice

# Clear existing prices
DevicePrice.objects.all().delete()

# Real-world device prices in INR (1 USD = 83 INR approx)
devices = [
    # Apple MacBooks
    {'brand': 'Apple', 'model_name': 'MacBook Air M1', 'processor': 'M1', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 70000, 'mint_price': 62000, 'overused_price': 45000, 'release_year': 2020},
    {'brand': 'Apple', 'model_name': 'MacBook Air M2', 'processor': 'M2', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 90000, 'mint_price': 78000, 'overused_price': 58000, 'release_year': 2022},
    {'brand': 'Apple', 'model_name': 'MacBook Pro M1', 'processor': 'M1', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 108000, 'mint_price': 91000, 'overused_price': 70000, 'release_year': 2020},
    {'brand': 'Apple', 'model_name': 'MacBook Pro M2', 'processor': 'M2', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 132000, 'mint_price': 116000, 'overused_price': 87000, 'release_year': 2022},
    
    # Dell Laptops
    {'brand': 'Dell', 'model_name': 'Inspiron 15 i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 40000, 'mint_price': 33000, 'overused_price': 23000, 'release_year': 2021},
    {'brand': 'Dell', 'model_name': 'XPS 13 i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 75000, 'mint_price': 62000, 'overused_price': 45000, 'release_year': 2021},
    {'brand': 'Dell', 'model_name': 'G15 Gaming i7 RTX3060', 'processor': 'i7', 'gpu': 'RTX3060', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 91000, 'mint_price': 78000, 'overused_price': 58000, 'release_year': 2022},
    {'brand': 'Dell', 'model_name': 'Inspiron 14 i3', 'processor': 'i3', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 29000, 'mint_price': 23000, 'overused_price': 15000, 'release_year': 2020},
    
    # HP Laptops
    {'brand': 'HP', 'model_name': 'Pavilion 15 i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 37000, 'mint_price': 31000, 'overused_price': 21000, 'release_year': 2021},
    {'brand': 'HP', 'model_name': 'Envy 13 i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 70000, 'mint_price': 58000, 'overused_price': 41000, 'release_year': 2021},
    {'brand': 'HP', 'model_name': 'Omen 15 i7 RTX3050', 'processor': 'i7', 'gpu': 'RTX3050', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 78000, 'mint_price': 66000, 'overused_price': 49000, 'release_year': 2022},
    {'brand': 'HP', 'model_name': 'Pavilion Gaming i5 GTX1650', 'processor': 'i5', 'gpu': 'GTX1650', 'ram_gb': 8, 'storage_gb': 512, 
     'pristine_price': 54000, 'mint_price': 45000, 'overused_price': 33000, 'release_year': 2020},
    
    # Lenovo Laptops
    {'brand': 'Lenovo', 'model_name': 'IdeaPad 3 i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 38000, 'mint_price': 32000, 'overused_price': 22000, 'release_year': 2021},
    {'brand': 'Lenovo', 'model_name': 'ThinkPad X1 i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 83000, 'mint_price': 70000, 'overused_price': 51000, 'release_year': 2021},
    {'brand': 'Lenovo', 'model_name': 'Legion 5 Ryzen7 RTX3060', 'processor': 'Ryzen7', 'gpu': 'RTX3060', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 95000, 'mint_price': 81000, 'overused_price': 59000, 'release_year': 2022},
    {'brand': 'Lenovo', 'model_name': 'IdeaPad Gaming Ryzen5 GTX1650', 'processor': 'Ryzen5', 'gpu': 'GTX1650', 'ram_gb': 8, 'storage_gb': 512, 
     'pristine_price': 51000, 'mint_price': 43000, 'overused_price': 31000, 'release_year': 2021},
    
    # Samsung Laptops
    {'brand': 'Samsung', 'model_name': 'Galaxy Book i5', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 43000, 'mint_price': 36000, 'overused_price': 25000, 'release_year': 2021},
    {'brand': 'Samsung', 'model_name': 'Galaxy Book Pro i7', 'processor': 'i7', 'gpu': 'Integrated', 'ram_gb': 16, 'storage_gb': 512, 
     'pristine_price': 73000, 'mint_price': 60000, 'overused_price': 44000, 'release_year': 2021},
    
    # Budget/Other Options
    {'brand': 'Other', 'model_name': 'Generic i3 Laptop', 'processor': 'i3', 'gpu': 'Integrated', 'ram_gb': 4, 'storage_gb': 256, 
     'pristine_price': 23000, 'mint_price': 18000, 'overused_price': 11000, 'release_year': 2020},
    {'brand': 'Other', 'model_name': 'Generic i5 Laptop', 'processor': 'i5', 'gpu': 'Integrated', 'ram_gb': 8, 'storage_gb': 256, 
     'pristine_price': 31000, 'mint_price': 25000, 'overused_price': 17000, 'release_year': 2020},
]

# Create device price entries
for device in devices:
    DevicePrice.objects.create(**device)
    print(f"Added: {device['brand']} {device['model_name']} - Pristine: Rs.{device['pristine_price']}")

print(f"\nSuccessfully added {len(devices)} device prices in INR!")
print("All prices are now in Indian Rupees (INR)")
