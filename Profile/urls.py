from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.profile, name='profile')
]