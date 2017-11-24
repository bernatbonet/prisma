"""
CRM models definition
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    cod_pos = models.CharField(max_length=6)
    provincia = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    movil = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    registro = models.CharField(max_length=250, null=True, blank=True)

class Modules(models.Model):
    """ Modulos de la aplicacion"""

    mod_apl = models.CharField(max_length=5)
    mod_codigo = models.CharField(max_length=20)
    mod_desc = models.CharField(max_length=250)
    mod_version = models.CharField(max_length=5)

class Roles(models.Model):
    """ Roles de la aplicacion"""

    emp_cod = models.CharField(max_length=5)
    rol_cod = models.CharField(max_length=20)
    rol_desc = models.CharField(max_length=250)

class EmpUsu(models.Model):
    """ Usuarios por empresa"""

    emp_cod = models.CharField(max_length=5)
    usu_cod = models.CharField(max_length=20)

class Usuario(models.Model):
    """ Usuarios de la aplicacion"""

    usu_cod = models.CharField(max_length=20)
    usu_nom = models.CharField(max_length=50)
    usu_idi = models.CharField(max_length=20)
    usu_email = models.CharField(max_length=250)
    usu_pass = models.CharField(max_length=20)

class ModRol(models.Model):
    """Modulos por rol"""

    mor_empcod = models.CharField(max_length=20)
    mor_modcod = models.CharField(max_length=20)
    mor_rolcod = models.CharField(max_length=20)
    mor_insercion = models.CharField(max_length=1)
    mor_borrado = models.CharField(max_length=1)
    mor_modificacion = models.CharField(max_length=1)
    mor_consulta = models.CharField(max_length=1)
    mor_exportacion = models.CharField(max_length=1)

class RolUsu(models.Model):
    """Roles por usuario"""

    rou_empcod = models.CharField(max_length=20)
    rou_rolcod = models.CharField(max_length=20)
    rou_usucod = models.CharField(max_length=20)
    rou_activo = models.CharField(max_length=1)