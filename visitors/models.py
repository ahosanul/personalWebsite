from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=120)
    address= models.TextField()
    age= models.IntegerField()

