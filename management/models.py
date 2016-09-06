from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, unique=True, blank=True, null=True,)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    photo = models.ImageField(upload_to='photo/', null=True, blank=True)

    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)

    user = models.OneToOneField( User, on_delete=models.CASCADE, primary_key=True, )

    USERNAME_FIELD = 'username'

    class Meta(object):
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = False

    def get_full_name(self):
        """
        Returns email instead of the fullname for the user.
        """
        return email_to_name(self.email)

    def get_short_name(self):
        """
        Returns the short name for the user.
        This function works the same as `get_full_name` method.
        It's just included for django built-in user comparability.
        """
        return self.get_full_name()

    def __str__(self):
        return self.email


class UserType(models.Model):

    user = models.OneToOneField( User, on_delete=models.CASCADE, primary_key=True, )

class UserStatus(models.Model):

    user = models.OneToOneField( User, on_delete=models.CASCADE, primary_key=True, )