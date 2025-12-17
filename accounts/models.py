from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')
    card_number = models.CharField(max_length=20, blank=True, verbose_name='Номер карты')
    cvc = models.CharField(max_length=4, blank=True, verbose_name='CVC')
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
    
    def __str__(self):
        return self.user.username