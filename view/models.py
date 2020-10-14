from django.db import models

# Create your models here.


class journals(models.Model):
    title = models.CharField(max_length=500)
    link= models.URLField()
    class Meta:
        db_table = "journals"

class conference(models.Model):
    title = models.CharField(max_length=500)
    class Meta:
        db_table = "conference"

class presentation(models.Model):
    title = models.CharField(max_length=500)
    class Meta:
        db_table = "presentation"


class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption