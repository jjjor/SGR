from django import forms
from .models import MealRequest

class MealRequestForm(forms.ModelForm):
    class Meta:
        model = MealRequest
        fields = ['meal_type', 'justification']

    

