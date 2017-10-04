# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import CompanySerializer
from .models import Company

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )
