from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=100)
    college_name = models.CharField(blank=True, max_length=100)
    phonenumber = models.CharField(blank=True, max_length=100)
    points = models.IntegerField(default=0)
    referral_code = models.CharField(max_length=7, unique=True)

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return self.name