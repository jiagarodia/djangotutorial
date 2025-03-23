from django.db import models
from django.contrib.auth.models import User

class Pofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pis')

    def __str__(self):
        return f'{self.user.username} Profile'