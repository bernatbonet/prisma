"""
CRM urls definition
Using routers would generate the followinf URL patterns:
  ^users/$        --> user-list
  ^users/{pk}$    --> user-detail
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
<<<<<<< HEAD
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ModulesApiView
=======
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .api import CompanyViewSet, UserViewSet
>>>>>>> 86a0b2d6e9464ad73e1255d005deaf3cd61deb99

urlpatterns = [
    # Maps to ModulesApiView.get and ModulesApiView.post
    url(r'^modules$', ModulesApiView.as_view()),
    # Maps to ModulesApiView.delete
    url(r'^modules/(?P<module_id>[0-9]+)$', ModulesApiView.as_view()),
]

<<<<<<< HEAD
urlpatterns = format_suffix_patterns(urlpatterns)
=======
urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token, name='get_auth_token'),
]

urlpatterns += router.urls
>>>>>>> 86a0b2d6e9464ad73e1255d005deaf3cd61deb99
