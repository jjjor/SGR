from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, View, CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy
from .models import MealRequest, Meal
from .forms import MealRequestForm, MealForm
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
            messages.error(request, "Já existe um usuário com esse usuário.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_student = True
        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')
    
    
class TodayMealView(TemplateView):
    template_name = 'today_meal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lunchs = Meal.objects.filter(meal_type='lunch')
        dinners = Meal.objects.filter(meal_type='dinner')

        context['lunch'] = lunchs
        context['dinner'] = dinners

        return context
    
class TodayMenuView(TemplateView):
    template_name = 'today_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        lunchs = Meal.objects.filter(meal_type='lunch')
        dinners = Meal.objects.filter(meal_type='dinner')

        context['lunch'] = lunchs
        context['dinner'] = dinners

        return context

    
    

class SelectDishView(View):
    def get(self, request, meal_id, meal_type):
      
        try:
            meal = Meal.objects.get(id=meal_id)
        except Meal.DoesNotExist:
            return redirect('today_menu') 


        if meal_type == 'lunch':
            request.session['selected_lunch'] = meal.id
        elif meal_type == 'dinner':
            request.session['selected_dinner'] = meal.id

       
        return redirect('today_menu')
    
    

class MealRequestCreateView(LoginRequiredMixin, CreateView):
    model = MealRequest
    form_class = MealRequestForm
    template_name = 'request_meal.html'
    success_url = reverse_lazy('my_requests')

    def form_valid(self, form):
  
        today = timezone.now().date()
        user = self.request.user
        existing_request = MealRequest.objects.filter(user=user, date=today).exists()
        
        if existing_request:
            messages.error(self.request, "Você já solicitou uma refeição para hoje.")
            return redirect('request_meal') 
        
       
        form.instance.user = self.request.user
        return super().form_valid(form)


class MealRequestListView(LoginRequiredMixin, ListView):
    model = MealRequest
    template_name = 'my_requests.html'
    context_object_name = 'meals'

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return MealRequest.objects.all()
        return MealRequest.objects.filter(user=self.request.user)


class MealRequestUpdateView(LoginRequiredMixin, UpdateView):
    model = MealRequest
    form_class = MealRequestForm
    template_name = 'request_meal.html'
    success_url = reverse_lazy('my_requests')

    def get_queryset(self):
        return MealRequest.objects.filter(user=self.request.user)


class MealRequestDeleteView(DeleteView):
    model = MealRequest
    success_url = reverse_lazy('my_requests')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        return MealRequest.objects.filter(user=self.request.user)
    
    
class MealRequestStatusUpdateView(View):
    def post(self, request, *args, **kwargs):
        meal_ids = request.POST.getlist('meal_ids')
        status = request.POST.getlist('status')

        for meal_id, new_status in zip(meal_ids, status):
            meal_request = MealRequest.objects.get(id=meal_id)

           
            if meal_request.user == request.user:
                messages.error(request, f"Você não pode alterar o status da sua própria solicitação de {meal_request.get_meal_type_display()}.")
                continue  # Pula para a próxima solicitação

            meal_request.status = new_status
            meal_request.save()

        
        messages.success(request, "Status das solicitações atualizados com sucesso!")
        
      
        return redirect('meal_requests')

    def get(self, request, *args, **kwargs):
    
        meal_requests = MealRequest.objects.all()
        return render(request, 'meal_requests.html', {'meal_requests': meal_requests})


    
class IndexView(TemplateView):

    template_name = 'base.html'


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'create_meal.html'
    success_url = reverse_lazy('list_meals') 

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            return redirect('home') 
        return super().form_valid(form)
    
class MealListView(ListView):
    model = Meal
    template_name = 'list_meals.html'
    context_object_name = 'meals'

class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = MealForm
    template_name = 'create_meal.html'
    success_url = reverse_lazy('list_meals')

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            return redirect('home') 
        return super().form_valid(form)
    
class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'confirm_delete_meal.html'
    success_url = reverse_lazy('list_meals')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def get_queryset(self):
    
        if not self.request.user.is_superuser:
            return Meal.objects.none()
        return Meal.objects.all()

class MyRequestsView(TemplateView):

    template_name = 'my_requests.html'

class RequestMealView(TemplateView):

    template_name = 'request_meal.html'
