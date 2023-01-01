from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField()
    avatar = models.ImageField(upload_to='profile_pic', default='download.png')
