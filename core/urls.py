from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    # authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('index/', IndexView.as_view(), name='index'),
    path('create-meal/', CreateMealView.as_view(), name='create_meal'),
    path('today-meal/', TodayMealView.as_view(), name='today_meal'),
    path('today-menu/', TodayMenuView.as_view(), name='today_menu'),
    path('my-requests/', MyRequestsView.as_view(), name='my_requests'),
    path('request-meal/', RequestMealView.as_view(), name='request_meal'),
    path('requests/', RequestsView.as_view(), name='requests'),
    
]

