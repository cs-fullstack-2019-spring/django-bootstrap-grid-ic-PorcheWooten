from django.db import models

# Create your models here.

class SignInModel(models.Model):
    USERNAME = models.CharField(max_length=200, default="")
    PASSWORD = models.CharField(max_length=200, default="")

class SignUpModel(models.Model):
    USERNAME = models.CharField(max_length=200, default="")
    EMAIL = models.EmailField(default="")
    PASSWORD = models.CharField(max_length=200, default="")
    CONFIRM_PASSWORD = models.CharField(max_length=200, default="")
