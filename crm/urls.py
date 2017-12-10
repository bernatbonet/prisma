"""
CRM urls definition
"""
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .api import CompanyViewSet, UserViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'user', UserViewSet)

urlpatterns = router.urls
