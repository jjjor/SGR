from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User

User = get_user_model()




class LoginView(TemplateView):

    template_name = 'login.html'

class RegisterView(TemplateView):

    template_name = "register.html" 

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ja existe saporr apoapoapsopso')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('usuario cadastrado')

    
class IndexView(TemplateView):

    template_name = 'base.html'

class CreateMealView(TemplateView):

    template_name = 'create_meal.html'

class TodayMealView(TemplateView):

    template_name = 'today_meal.html'

class TodayMenuView(TemplateView):

    template_name = 'today_menu.html'

class MyRequestsView(TemplateView):

    template_name = 'my_requests.html'

class RequestMealView(TemplateView):

    template_name = 'request_meal.html'

class RequestsView(TemplateView):

    template_name = 'requests.html'
