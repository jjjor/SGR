from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, MealRequest

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

# Register your models here.
admin.site.register(CustomUser, MyUserAdmin)