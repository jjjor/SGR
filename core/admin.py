from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, MealRequest, Meal

class MyUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_holder', 'is_student',)}),
    )

@admin.register(MealRequest)
class MealRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'meal_type', 'justification')
    search_fields = ('user__username', 'meal_type', 'justification')
    list_filter = ('meal_type', 'justification')  

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("meal_type", "description")  # Campos que aparecem na lista
    search_fields = ("meal_type", "description")  

# Register your models here.
admin.site.register(CustomUser, MyUserAdmin)