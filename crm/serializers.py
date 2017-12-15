# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Company, Modules
from core.models import User

class CompanySerializer(serializers.ModelSerializer):
    """
    Create a serializer for company model
    """

    class Meta:
        """Meta definition for company model"""
        model = Company
        fields = ('id', 'cif', 'nombre', 'nombre_fiscal', 'tipo_via', 'direccion1',
                  'direccion2', 'direccion3', 'numero', 'poblacion', 'cod_pos', 'provincia',
                  'pais', 'telefono', 'fax', 'email', 'registro')

class ModuleSerializer(serializers.ModelSerializer):
    """
    Create a serializer for modules model.
    """
    class Meta:
        """ Meta definition for module model """
        model = Modules
        fields = ('id', 'mod_apl', 'mod_codigo', 'mod_desc', 'mod_version')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined',
                'last_login')
