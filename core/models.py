"""
Core models
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from prisma.settings import base

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext as _

from rest_framework.authtoken.models import Token

class User(AbstractUser):
    """
    New fields for user model
    """
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def _create_user(self, username, password, email, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password
        """
        if not username:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, 
                          email=email,
                          is_staff=True,
                          is_superuser=is_superuser,
                          is_active=True,
                          date_joined=timezone.now(),
                          **extra_fields)
        user.set_password(password)                          
        user.save(using=self._db)
        return user
    
    def create_user(self, username, password, email, **extra_fields):
        return _create_user(username, password, email, False, **extra_fields)
    
    def create_superuser(self, username, password, email, **extra_fields):
        return _create_user(username, password, email, True, **extra_fields)

    @receiver(post_save, sender=base.AUTH_USER_MODEL)
    def create_auth_token(self, instance=None, created=False, **kwargs):
        """
        This code is triggered whenever a new user has been created
            and saved to the database
        """
        if created:
            Token.objects.create(user=instance)
