from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class MailModel(AbstractBaseUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.username
    
# Create your models here.
