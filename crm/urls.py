"""
CRM urls definition
"""
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .api import CompanyViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet)

urlpatterns = router.urls
