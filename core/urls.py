from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    # authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('index/', IndexView.as_view(), name='index'),
    path('create-meal/', MealCreateView.as_view(), name='create_meal'),
    path('today-meal/', TodayMealView.as_view(), name='today_meal'),
    path('today-menu/', TodayMenuView.as_view(), name='today_menu'),
    path('request-meal/', RequestMealView.as_view(), name='request_meal'),

    path('request_meal/', MealRequestCreateView.as_view(), name='request_meal'),
    path('my_requests/', MealRequestListView.as_view(), name='my_requests'),
    path('edit/<int:pk>/', MealRequestUpdateView.as_view(), name='update_meal'),
    path('delete/<int:pk>/', MealRequestDeleteView.as_view(), name='delete_meal'),

    path('meal_requests/', MealRequestStatusUpdateView.as_view(), name='meal_requests'),
    
    path('meal/create/', MealCreateView.as_view(), name='create_meal'),
    path('list_meals/', MealListView.as_view(), name='list_meals'),
    path('meal/<int:pk>/edit/', MealUpdateView.as_view(), name='edit_meal'),
    path('meal/<int:pk>/delete/', MealDeleteView.as_view(), name='delete_meal'),
]

