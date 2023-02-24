from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


