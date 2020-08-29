from django.contrib import admin
from django.urls import path
from camp import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('fashion', views.fashion, name='fashion'),
    #path('travel', views.travel, name='travel'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    #path('register',views.register,name="register"),
]
