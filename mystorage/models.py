from django.db import models
from django.conf import settings


class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = "images")
    desc = models.CharField(max_length = 100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
    myfile = models.FileField(blank = False, null = False, upload_to= "files")
    desc = models.CharField(max_length = 100)