from django.contrib import admin
from core.models import Snack, RequestSnack, User

admin.site.register(User)
@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ("description", "likes", "snack_to_day", "type", "active")

@admin.register(RequestSnack)
class RequestSnackAdmin(admin.ModelAdmin):
    list_display = ("user", "data", "justification", "status", "type")