from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('publications', views.publicatin, name='publication'),

]