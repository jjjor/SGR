import os
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.conf import settings

def get_file_path(instance, filename):
    # Define o caminho de upload
    return os.path.join('uploads/', str(instance.user.id), filename)

class MealRequest(models.Model):
    MEAL_CHOICES = [
        ('jantar', 'Jantar'),
        ('almoco', 'Almoço'),
    ]

    JUSTIFICATION_CHOICES = [
        ('turno_inverso', 'Aula em turno inverso'),
        ('esporte', 'Práticas esportivas'),
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('deferido', 'Deferido'),
        ('indeferido', 'Indeferido'),
    ]


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)
    justification = models.CharField(max_length=20, choices=JUSTIFICATION_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.user} - {self.justification} - {self.meal_type}"
    

class Meal(models.Model):
    MEAL_CHOICES = (
        ('lunch', 'Almoço'),
        ('dinner', 'Janta'),
    )

    meal_type = models.CharField(max_length=6, choices=MEAL_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='meals_images/')
    
    def __str__(self):
        return f"{self.get_meal_type_display()} - {self.description[:20]}"
    


class CustomUser(AbstractUser):
    is_holder = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)