"""
Core urls definition
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token, name='get_auth_token'),
]