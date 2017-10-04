# -*- coding: utf-8 -*-
from .api import CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'company', CompanyViewSet)

urlpatterns = router.urls
