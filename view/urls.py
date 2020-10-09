from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('presentation', views.presentation, name='presentation'),
    path('research', views.research , name='research'),
    path('teaching', views.teaching, name='teaching'),
    path('contact', views.contact, name='contact'),
    path('publications', views.publicatin, name='publication'),

]