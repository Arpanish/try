from django.db import models


class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=15)

# Create your models here.
