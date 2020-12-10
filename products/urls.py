from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]