from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    """Модель автомобиля для аренды"""
    VEHICLE_TYPES = [
        ('SUV', 'Внедорожник'),
        ('PICKUP', 'Пикап'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES, verbose_name='Тип')
    year = models.IntegerField(verbose_name='Год выпуска')
    capacity = models.IntegerField(verbose_name='Вместимость (чел.)')
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за час ($)')
    image = models.ImageField(upload_to='vehicles/', blank=True, null=True, verbose_name='Изображение')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')
    is_available = models.BooleanField(default=True, verbose_name='Доступен')
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
    
    def __str__(self):
        return self.name