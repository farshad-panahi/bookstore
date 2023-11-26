from django.contrib.auth.models import AbstractUser
from django.db import models


class ThisUser(AbstractUser):
    name = models.CharField(
        blank=True,
        null=True,
        max_length=200,
    )