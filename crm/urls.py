"""
CRM urls definition
Using routers would generate the followinf URL patterns:
  ^users/$        --> user-list
  ^users/{pk}$    --> user-detail
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ModulesApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .api import CompanyViewSet, UserViewSet

urlpatterns = [
    # Maps to ModulesApiView.get and ModulesApiView.post
    url(r'^modules$', ModulesApiView.as_view()),
    # Maps to ModulesApiView.get and ModulesApiView.delete
    url(r'^modules/(?P<module_id>[0-9]+)$', ModulesApiView.as_view()),
]
