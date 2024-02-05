from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username