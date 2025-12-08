from django.contrib import admin
from .models import Facility, Device, RecyclingLog

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
    list_display = ['device_brand', 'device_processor', 'estimated_value', 'carbon_saved', 'created_at']
    list_filter = ['created_at']
