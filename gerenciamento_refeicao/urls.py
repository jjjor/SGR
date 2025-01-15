"""
URL configuration for gerenciamento_refeicao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import core
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create-meal/', views.create_meal, name='create_meal'),
    path('today_meal/', views.today_meal, name='today_meal'),
    path('today_menu/', views.today_menu, name='today_menu'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('request_meal/', views.request_meal, name='request_meal'),
    path('requests/', views.requests, name='requests'),
]
