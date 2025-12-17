from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vehicle', 'start_date', 'end_date', 'total_price', 'status')
    list_filter = ('status', 'start_date', 'vehicle')
    search_fields = ('user__username', 'vehicle__name')
    list_editable = ('status',)
    date_hierarchy = 'created_at'