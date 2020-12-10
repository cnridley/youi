from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.progression_pictures, name='progression_pictures'),
    path('delete/<int:progressionpicture_id>/', views.delete_picture, name='delete_picture'),
    path('edit/<int:progression_id>/', views.edit_picture, name='edit_picture'),
]