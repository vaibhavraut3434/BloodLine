from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('fashion', views.register, name='register'),
    path('auth2', views.auth2, name='auth12'),
    path('dash', views.dashboard, name='dashboard'),
    path('entry', views.entry, name='entry'),
    path('entry/update', views.entry, name='entry'),
    
    
    path('orgform', views.orgform, name='orgform'),
    path('organdata', views.organdata, name='organdata'),
    
    
    #path('dash', views.dashboard, name='dashboard'),
    
]
