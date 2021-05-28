from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ' کاربران'
        verbose_name_plural = ' کاربران'

    def __str__(self):
        return self.user.username
