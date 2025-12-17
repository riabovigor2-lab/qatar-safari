
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from bookings.models import Booking

def register(request):

    if request.method == 'POST':
      
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        card_number = request.POST.get('card_number', '')
        cvc = request.POST.get('cvc', '')
        
      
        if not all([username, password1, password2, email, phone, address]):
            messages.error(request, 'Заполните все обязательные поля!')
            return render(request, 'registration/register.html')
        
      
        if password1 != password2:
            messages.error(request, 'Пароли не совпадают!')
            return render(request, 'registration/register.html')
        
     
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует!')
            return render(request, 'registration/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует!')
            return render(request, 'registration/register.html')
        
        try:
         
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
           
            profile = UserProfile.objects.create(
                user=user,
                phone=phone,
                address=address,
                card_number=card_number,
                cvc=cvc
            )
            
        
            login(request, user)
            messages.success(request, 'Регистрация успешна! Добро пожаловать!')
            return redirect('dashboard')  
            
        except Exception as e:
            messages.error(request, f'Ошибка при регистрации: {str(e)}')
            return render(request, 'registration/register.html')
    
   
    return render(request, 'registration/register.html')

@login_required
def profile(request):
  
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Профиль обновлен!')
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=user_profile)
    
    return render(request, 'accounts/profile.html', {'form': profile_form})

@login_required
def dashboard(request):
   
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
  
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    total_bookings = bookings.count()
    active_bookings = bookings.filter(status__in=['pending', 'confirmed']).count()
    completed_bookings = bookings.filter(status='completed').count()
    
    return render(request, 'accounts/dashboard.html', {
        'user_profile': user_profile,
        'bookings': bookings[:5],  
        'total_bookings': total_bookings,
        'active_bookings': active_bookings,
        'completed_bookings': completed_bookings,
    })