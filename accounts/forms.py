
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
  
    password1 = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'required': True
        })
    )
    
    password2 = forms.CharField(
        label='Подтверждение пароля', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'required': True
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com',
                'required': True
            }),
        }
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email адрес',
        }
    
    def clean_password2(self):
      
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']
    
    def clean_username(self):
      
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует.')
        return username
    
    def clean_email(self):
        
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует.')
        return email

class UserProfileForm(forms.ModelForm):
   
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'card_number', 'cvc']
        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '89091234567',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Введите ваш адрес',
                'required': True
            }),
            'card_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '1234 5678 9012 3456',
                'required': False
            }),
            'cvc': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': '123',
                'required': False,
                'maxlength': '3'
            }),
        }
        labels = {
            'phone': 'Телефон *',
            'address': 'Адрес *',
            'card_number': 'Номер карты',
            'cvc': 'CVC код',
        }
        help_texts = {
            'phone': 'Обязательное поле',
            'address': 'Обязательное поле',
        }


class CompleteRegistrationForm(forms.Form):
  

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя',
            'required': True
        }),
        label='Имя пользователя *'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com',
            'required': True
        }),
        label='Email *'
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'required': True
        }),
        label='Пароль *'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'required': True
        }),
        label='Подтверждение пароля *'
    )
    
 
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '89091234567',
            'required': True
        }),
        label='Телефон *'
    )
    
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Введите ваш адрес',
            'required': True
        }),
        label='Адрес *'
    )
    
    card_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1234 5678 9012 3456'
        }),
        label='Номер карты'
    )
    
    cvc = forms.CharField(
        max_length=4,
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '123',
            'maxlength': '3'
        }),
        label='CVC код'
    )
    
    def clean(self):
   
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        
      
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Пароли не совпадают.')
        
        
        if username and User.objects.filter(username=username).exists():
            self.add_error('username', 'Пользователь с таким именем уже существует.')
       
        if email and User.objects.filter(email=email).exists():
            self.add_error('email', 'Пользователь с таким email уже существует.')
        
        return cleaned_data