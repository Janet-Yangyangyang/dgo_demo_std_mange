from django.db import models


# Create your models here.

class TestUser(models.Model):
    username = models.CharField(max_length=64)
    pwd = models.CharField(max_length=32)
