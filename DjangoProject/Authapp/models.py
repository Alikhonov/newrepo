from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #creating using already existing user and adding extra fields to this user model
    Portfolio = models.URLField(blank=True)
    profile_pics = models.ImageField(upload_to='profile_pics', blank=True)
    
