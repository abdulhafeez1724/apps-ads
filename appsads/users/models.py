from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.
class  NewUser(AbstractUser):

    class Platform(models.TextChoices):
        ANDROID = 'android', _('ANDROID')
        IOS = 'ios', _('IOS')
        
    name  = models.CharField(max_length=150, blank=False)
    platform = models.CharField('Platform', max_length=50, choices=Platform.choices, default=Platform.ANDROID, blank=False)