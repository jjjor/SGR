from django import forms
from .models import MealRequest, Meal

class MealRequestForm(forms.ModelForm):
    class Meta:
        model = MealRequest
        fields = ['meal_type', 'justification']

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_type', 'description', 'image']
    

