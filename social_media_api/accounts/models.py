from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='images/')
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)