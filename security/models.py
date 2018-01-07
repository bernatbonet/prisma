# -*- coding: utf-8 -*-
"""
Paquete para la definición de los modelos
de la aplicación Security
"""
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .managers import PaqueteManager

class Paquete(models.Model):
    """
    Paquetes: conjunto de módulos
    """

    cod_paq = models.CharField(
        verbose_name=_('Código de paquete'),
        help_text=_('Introduce el código del paquete'),
        max_length=5,
        unique=True,
        null=False)
    nom_paq = models.CharField(
        verbose_name=_('Nombre del paquete'),
        help_text=_('Introduce el nombre del paquete'),
        max_length=100)
    des_paq = models.TextField(
        verbose_name=_('Descripción del paquete'),
        help_text=_('Introduzca la descripción del paquete'),
        max_length=255
    )

    # Managers
    objects = PaqueteManager()

    class Meta(object):
        """Meta información del modelo"""
        verbose_name = 'paquete'
        verbose_name_plural = 'paquetes'

    # Functions
    def __unicode__(self):
        return _('Paquete %s') % (self.nom_paq)

    def save(self, *args, **kwargs):
        super(Paquete, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Url para acceder al objeto por HTTP"""
        return reverse('paquete.views.details', args=[str(self.cod_paq)])
