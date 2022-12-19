from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.portfolio, name='portfolio'),
    path('services', views.services, name='services')
]