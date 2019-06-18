from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):

    is_active = models.BooleanField(default=True)

    # Extend the django user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # One to many relationships

    def __str__(self):
        return self.user.username + " (User Info)"
