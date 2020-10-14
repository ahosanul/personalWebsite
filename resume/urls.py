from django.contrib import admin
from django.urls import path,include

urlpatterns = [
     path('', include('view.urls')),
    path('visitors', include('visitors.urls')),
    path('adminarup', admin.site.urls),
]
