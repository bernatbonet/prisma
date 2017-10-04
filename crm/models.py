# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    """ Company model"""
    
    cif = models.CharField(max_length=15)
    nombre = models.CharField(max_length=250)
    nombre_fiscal = models.CharField(max_length=250)
    tipo_via = models.CharField(max_length=5)
    direccion1 = models.CharField(max_length=250)
    direccion2 = models.CharField(max_length=250, null=True, blank=True)
    direccion3 = models.CharField(max_length=250, null=True, blank=True)
    numero = models.CharField(max_length=15)
    poblacion = models.CharField(max_length=250)
    cp = models.CharField(max_length=6)
    provincia = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    movil = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    registro = models.CharField(max_length=250, null=True, blank=True)