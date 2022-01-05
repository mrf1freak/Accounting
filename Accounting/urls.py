"""Accounting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('GeneralEntry.urls')),
    path('admin/', admin.site.urls),
    path('product/', include('Product.urls')),
    path('product-entry/', include('ProductEntry.urls')),
    path('general-entry/', include('GeneralEntry.urls')),
    path('account/', include('Account.urls')),
    path('users/login/', auth_views.LoginView.as_view(redirect_field_name='/')),
    path('users/logout/', auth_views.LogoutView.as_view(next_page='/users/login/')),
    
]