from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('presentation', views.presentationaward, name='presentationaward'),
    path('research', views.research , name='research'),
    path('teaching', views.teaching, name='teaching'),
    path('contact', views.contact, name='contact'),
    path('publications', views.publicatin, name='publication'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)