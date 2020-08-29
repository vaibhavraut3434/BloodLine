from django.contrib import admin
from django.urls import path
from host import views

urlpatterns = [
    path('bloodcamp', views.bloodcamp, name='bloodcamp'),
    path('auth3', views.auth3, name='auth3'),
    path('entry', views.entry, name='entry'),
    
    
]
