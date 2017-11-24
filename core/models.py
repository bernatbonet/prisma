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
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    """
    New fields for user model
    """
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    @receiver(post_save, sender=base.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        """
        This code is triggered whenever a new user has been created 
            and saved to the database
        """
        if created:
            Token.objects.create(user=instance)
