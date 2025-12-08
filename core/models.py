from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    
    class Meta:
        verbose_name_plural = "Facilities"
    
    def __str__(self):
        return self.name

class Device(models.Model):
    BRAND_CHOICES = [
        ('Apple', 'Apple'),
        ('Dell', 'Dell'),
        ('HP', 'HP'),
        ('Lenovo', 'Lenovo'),
        ('Samsung', 'Samsung'),
        ('Other', 'Other'),
    ]
    
    PROCESSOR_CHOICES = [
        ('i3', 'Intel i3'),
        ('i5', 'Intel i5'),
        ('i7', 'Intel i7'),
        ('i9', 'Intel i9'),
        ('Ryzen3', 'AMD Ryzen 3'),
        ('Ryzen5', 'AMD Ryzen 5'),
        ('Ryzen7', 'AMD Ryzen 7'),
        ('M1', 'Apple M1'),
        ('M2', 'Apple M2'),
    ]
    
    GPU_CHOICES = [
        ('Integrated', 'Integrated'),
        ('GTX1650', 'GTX 1650'),
        ('GTX1660', 'GTX 1660'),
        ('RTX3050', 'RTX 3050'),
        ('RTX3060', 'RTX 3060'),
        ('RTX4060', 'RTX 4060'),
    ]
    
    MATERIAL_CHOICES = [
        ('Plastic', 'Plastic'),
        ('Aluminum', 'Aluminum'),
        ('Mixed', 'Mixed'),
    ]
    
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    processor = models.CharField(max_length=50, choices=PROCESSOR_CHOICES)
    gpu = models.CharField(max_length=50, choices=GPU_CHOICES)
    age_years = models.IntegerField()
    weight_kg = models.FloatField()
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES)
    
    def __str__(self):
        return f"{self.brand} - {self.processor}"

class RecyclingLog(models.Model):
    device_brand = models.CharField(max_length=50)
    device_processor = models.CharField(max_length=50)
    estimated_value = models.FloatField()
    carbon_saved = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.device_brand} - {self.created_at.strftime('%Y-%m-%d')}"
