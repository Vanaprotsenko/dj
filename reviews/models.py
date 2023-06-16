from django.db import models


class Revie(models.Model):
   
   review = models.CharField(max_length=255)
   username = models.CharField(max_length=255)

