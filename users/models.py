from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ADMIN = 1
    MANAGER = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MANAGER, 'manager'),
        (USER, 'user')
    )
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=True, null=True, default=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email