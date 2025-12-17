# main/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicle

def home(request):
    """Главная страница (сафари по дюнам)"""
    return render(request, 'home.html')

def catalog(request):
    """Страница каталога (выберите внедорожник)"""
    vehicles = Vehicle.objects.filter(is_available=True)
    return render(request, 'catalog.html', {'vehicles': vehicles})

def cars(request):
    """Страница всех автомобилей"""
    vehicles = Vehicle.objects.filter(is_available=True)
    return render(request, 'cars.html', {'vehicles': vehicles})

def vehicle_detail(request, vehicle_id):
    """Детальная страница автомобиля"""
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, is_available=True)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})