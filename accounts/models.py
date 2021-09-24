from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import Usermanger

class user(AbstractUser):
    username = None
    last_login = None
    email = models.EmailField(verbose_name='email', unique=True)
    date_joined = models.DateTimeField(verbose_name="Add joined date", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    mobile = models.IntegerField()

    objects = Usermanger()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name",]
