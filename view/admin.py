from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(journals)
admin.site.register(conference)
admin.site.register(presentation)
admin.site.register(Video)

