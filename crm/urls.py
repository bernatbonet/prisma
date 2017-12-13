"""
CRM urls definition
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .api import CompanyViewSet, UserViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token, name='get_auth_token'),
]

urlpatterns += router.urls