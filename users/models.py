
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'ADMIN'),
        ('USER', 'USER'),
        ('BUSINESS', 'BUSINESS'),
        ('TALENT', 'TALENT')
    )
    first_name = models.CharField(max_length=254, default="John")
    last_name = models.CharField(max_length=254, default="Doe")
    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address")
    role = models.CharField(max_length=8, choices=ROLES, default="USER")

    USERNAME_FIELD = "username"  # e.g: "username", "email"
    EMAIL_FIELD = "email"  # e.g: "email", "primary_email"

    def __str__(self):
        return self.username
