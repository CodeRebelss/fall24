from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.IntegerField()