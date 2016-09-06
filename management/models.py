from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserType(models.Model):

    objects = models.Manager()

    name = models.CharField(_('name'), max_length=30, unique=True, blank=True, null=True,)


    def __str__(self):
        return self.name


class UserStatus(models.Model):

    objects = models.Manager()

    name = models.CharField(_('name'), max_length=30, unique=True, blank=True, null=True,)


    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, unique=True, blank=True, null=True,)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    photo = models.ImageField(upload_to='photo/', null=True, blank=True)

    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)

    is_staff = models.BooleanField(_('staff status'), default=False,)

    user_type = models.ForeignKey( UserType, null=True, )
    user_status = models.ForeignKey( UserStatus, null=True, )

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta(object):
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = False

    def __str__(self):
        return self.username


