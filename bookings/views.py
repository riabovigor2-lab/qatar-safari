
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Booking
from main.models import Vehicle

@login_required
def my_bookings(request):
   
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def create_booking(request, vehicle_id):

    vehicle = get_object_or_404(Vehicle, id=vehicle_id, is_available=True)
    
    if request.method == 'POST':
        try:
            start_date_str = request.POST.get('start_date')
            end_date_str = request.POST.get('end_date')
            
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
            
        
            hours = (end_date - start_date).total_seconds() / 3600
            total_price = float(hours) * float(vehicle.price_per_hour)
            
           
            booking = Booking.objects.create(
                user=request.user,
                vehicle=vehicle,
                start_date=start_date,
                end_date=end_date,
                total_price=total_price,
                status='pending'
            )
            
            messages.success(request, 'Бронирование создано! Ожидайте подтверждения.')
            return redirect('my_bookings')
            
        except Exception as e:
            messages.error(request, f'Ошибка при создании бронирования: {str(e)}')
   
    tomorrow = timezone.now() + timedelta(days=1)
    day_after = tomorrow + timedelta(days=1)
    
    return render(request, 'bookings/create_booking.html', {
        'vehicle': vehicle,
        'default_start': tomorrow.strftime('%Y-%m-%d'),
        'default_end': day_after.strftime('%Y-%m-%d')
    })

@login_required
def cancel_booking(request, booking_id):
  
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'pending' or booking.status == 'confirmed':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Бронирование отменено.')
    
    return redirect('my_bookings')