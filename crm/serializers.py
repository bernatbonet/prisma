# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Company

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'cif', 'nombre', 'nombre_fiscal',
            'tipo_via', 'direccion1', 'direccion2', 'direccion3',
            'numero', 'poblacion', 'cp', 'provincia', 'pais',
            'telefono', 'fax', 'email', 'registro')
