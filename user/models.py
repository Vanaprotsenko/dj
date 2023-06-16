from django.db import models



# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.IntegerField()
    confirm_password = models.IntegerField()
    review = models.CharField(max_length=255)
