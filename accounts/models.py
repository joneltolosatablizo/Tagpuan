from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'age']
    USERNAME_FIELD = 'username'
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True)
