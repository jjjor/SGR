from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('core.urls')),
    path('admin/', admin.site.urls),
]
