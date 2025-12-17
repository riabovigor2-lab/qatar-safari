from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'year', 'capacity', 'price_per_hour', 'is_available')
    list_filter = ('vehicle_type', 'year', 'is_available')
    search_fields = ('name', 'description')
    list_editable = ('is_available', 'price_per_hour')