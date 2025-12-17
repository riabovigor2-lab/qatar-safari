# main/urls.py - добавляем новый путь
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('cars/', views.cars, name='cars'),  # НОВЫЙ
    path('vehicle/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
]

