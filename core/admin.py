from django.contrib import admin
from .models import Facility, Device, RecyclingLog, UserProfile, DevicePrice

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude', 'phone']
    search_fields = ['name', 'address']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['brand', 'processor', 'gpu', 'age_years', 'weight_kg']
    list_filter = ['brand', 'processor']

@admin.register(RecyclingLog)
class RecyclingLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'device_brand', 'device_processor', 'estimated_value', 'carbon_saved', 'created_at']
    list_filter = ['created_at', 'user']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_devices_recycled', 'total_value_earned', 'total_carbon_saved']

@admin.register(DevicePrice)
class DevicePriceAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model_name', 'processor', 'gpu', 'pristine_price', 'mint_price', 'overused_price', 'release_year']
    list_filter = ['brand', 'processor', 'release_year']
    search_fields = ['brand', 'model_name']
