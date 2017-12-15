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

urlpatterns = [
    # Maps to ModulesApiView.get and ModulesApiView.post
    url(r'^modules$', ModulesApiView.as_view()),
    # Maps to ModulesApiView.delete
    url(r'^modules/(?P<module_id>[0-9]+)$', ModulesApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
