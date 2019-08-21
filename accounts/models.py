from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import datetime
from django.utils import timezone


def random_field():
    return random.randint(1, 100)


class CustomUser(AbstractUser):
    birthday = models.DateField(default=timezone.now())
    random_field = models.IntegerField(default=random_field)

    class Meta:
        db_table = 'auth_user'
