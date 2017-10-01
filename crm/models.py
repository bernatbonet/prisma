# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    """ Company model"""

    cif = models.CharField(max_length=15)
    nombre_fiscal = models.ChariField(max_length=250)
    tipo_via = models.CharField(max_length=5)
    direccion1 = models.CharField(max_length=250)
    direccion2 = models.CharField(max_length=250)
    direccion3 = models.CharField(max_length=250)
    poblacion = models.CharField(max_length=250)
    cp = models.CharField(max_length=6)
    provincia = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    movil = models.CharField(max_length=20)
    email = models.CharField(max_length=250)