from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomBaseUserManager

class CustomUser(AbstractUser, PermissionsMixin):
    first_name = None
    last_name = None

    email = models.EmailField(_("Email"), unique=True)
    name = models.CharField("Nome", max_length=120, null=False, blank=False, default="")
    username = models.CharField("Usuário", max_length=14, unique=True, null=False, blank=False, default="")
    avatar = models.ImageField(upload_to='avatar/user', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomBaseUserManager()
    
    def __str__(self):
        return self.email