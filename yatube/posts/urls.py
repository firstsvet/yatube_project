# posts/urls.py
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    
    path('group/<slug:slug>/', views.group_posts)   
] 