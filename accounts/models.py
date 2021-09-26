from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import Usermanger
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    REQUIRED_FIELDS = ["first_name","last_name","mobile"]

class Profile(models.Model):
    user  = models.OneToOneField(user, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=8)
    profile_pic = models.FileField(upload_to="profile_pics")

@receiver(post_save, sender=user)
def create_or_save_user_profile(sender, created, instance,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
