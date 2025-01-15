from django.contrib import admin
from core.models import Snack, RequestSnack
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class MyUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_holder', 'is_student',)}),
    )

# Register your models here.
admin.site.register(CustomUser, MyUserAdmin)

@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ("description", "likes", "snack_to_day", "type", "active")

@admin.register(RequestSnack)
class RequestSnackAdmin(admin.ModelAdmin):
    list_display = ("user", "data", "justification", "status", "type")