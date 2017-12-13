# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, permissions

from .serializers import CompanySerializer, UserSerializer
from .models import Company, User

class CompanyViewSet(ModelViewSet):
    """ Viewset for company model"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )

class UserViewSet(ModelViewSet):
    """ Viewset for user model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'username')
