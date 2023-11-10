from django.contrib import admin
from django.urls import path, include
from app_GAALK import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_GAALK.urls')),
]