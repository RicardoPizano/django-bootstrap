# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager
from bootstrap import constants
from bootstrap.enums import Roles


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('nombre'), max_length=60)
    last_name = models.CharField(_('apellido'), max_length=60)
    phone = models.CharField(_('teléfono'), max_length=14)
    email = models.EmailField(_('correo electrónico'), unique=True)
    role = models.IntegerField(_('rol'), choices=Roles.choices, default=Roles.Client)
    is_active = models.BooleanField(_('está activo'), default=True)
    created_at = models.DateTimeField(_(constants.created_at_field_text), auto_now_add=True)
    deleted_at = models.DateTimeField(_(constants.deleted_at_field_text), null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_role(self):
        return Roles.choices[self.role - 1][1]

    def get_full_name(self):
        return '{} {}'.format(self.name, self.last_name)

    def __str__(self):
        return '{}'.format(self.email)


class Token(models.Model):
    user = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)
    token = models.TextField(_('token'))
    ip = models.CharField(_('host'), max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(_(constants.created_at_field_text), auto_now_add=True)
    deleted_at = models.DateTimeField(_(constants.deleted_at_field_text), null=True)
