"""
Setting exposed CRM models
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Company, Modules, Roles

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('cif', 'nombre', 'tipo_via', 'direccion1', 'cod_pos', 'provincia')

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display = ('mod_apl', 'mod_codigo', 'mod_desc', 'mod_version')

admin.site.register(Roles)
