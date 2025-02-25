from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    # authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('index/', IndexView.as_view(), name='index'),
    path('create-meal/', CreateMealView.as_view(), name='create_meal'),
    path('today-meal/', TodayMealView.as_view(), name='today_meal'),
    path('today-menu/', TodayMenuView.as_view(), name='today_menu'),
    path('my-requests/', MyRequestsView.as_view(), name='my_requests'),
    path('request-meal/', RequestMealView.as_view(), name='request_meal'),
    path('requests/', RequestsView.as_view(), name='requests'),

    path('request/', MealRequestCreateView.as_view(), name='request_meal'),
    path('list/', MealRequestListView.as_view(), name='list_meals'),
    path('edit/<int:pk>/', MealRequestUpdateView.as_view(), name='update_meal'),
    path('delete/<int:pk>/', MealRequestDeleteView.as_view(), name='delete_meal'),
    
]

