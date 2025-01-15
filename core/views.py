from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html', {})

def create_meal(request):
    return render(request, 'create_meal.html', {})

def today_meal(request):
    return render(request, 'today_meal.html', {})

def today_menu(request):
    return render(request, 'today_menu.html', {})

def my_requests(request):
    return render(request, 'my_requests.html', {})

def request_meal(request):
    return render(request, 'request_meal.html', {})

def requests(request):
    return render(request, 'requests.html', {})