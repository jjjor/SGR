from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, View, CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import MealRequest
from .forms import MealRequestForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class LoginView(TemplateView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'base.html')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return redirect('login')
        
        
class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class RegisterView(TemplateView):
    template_name = "register.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Já existe um usuário com esses dados.")
            return redirect('register')  # Redireciona para a mesma página

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login') 
    

# View para criar uma solicitação de refeição
class MealRequestCreateView(LoginRequiredMixin, CreateView):
    model = MealRequest
    form_class = MealRequestForm
    template_name = 'request_meal.html'
    success_url = reverse_lazy('list_meals')

    def form_valid(self, form):
        # Atribui o usuário logado à solicitação de refeição
        form.instance.user = self.request.user
        return super().form_valid(form)

# View para listar todas as solicitações do usuário
class MealRequestListView(LoginRequiredMixin, ListView):
    model = MealRequest
    template_name = 'list_meals.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return MealRequest.objects.filter(user=self.request.user)

# View para editar uma solicitação de refeição
class MealRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = MealRequest
    form_class = MealRequestForm
    template_name = 'request_meal.html'
    success_url = reverse_lazy('list_meals')

    def get_queryset(self):
        # Garante que o usuário só possa editar suas próprias solicitações
        return MealRequest.objects.filter(user=self.request.user)

# View para excluir uma solicitação de refeição
class MealRequestDeleteView(DeleteView):
    model = MealRequest
    success_url = reverse_lazy('list_meals') 
    template_name = None 

    def get_queryset(self):
        # Garante que o usuário só possa excluir suas próprias solicitações
        return MealRequest.objects.filter(user=self.request.user)
    






    
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
