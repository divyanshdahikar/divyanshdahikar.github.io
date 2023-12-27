from django.db import models

# Create your models here.

class Image(models.Model):
    photo = models.ImageField(upload_to = 'myimage')  #it will createfolder and save the image here.
    date = models.DateTimeField(auto_now_add = True)
