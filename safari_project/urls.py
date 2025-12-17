
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),  
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
 path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', accounts_views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)