# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

from django.test import TestCase
from security.models import Paquete


class PaqueteTestCase(TestCase):
    """
    Test para el modelo paquete
    """
    def crear_paquete(self, codpaq, nompaq, despaq):
        """
        Procedimiento para crear un paquete
        """
        try:
            return Paquete.objects.create(
                cod_paq=codpaq,
                nom_paq=nompaq,
                des_paq=despaq)
        except Exception:
            return Exception
    
    def test_paquete(self):
        """
        Test para la creación de un paquete
        con un len(codpaq)>5
        """
        # -------------------------------------------
        # Len(cod_paq) > 5
        paquete = self.crear_paquete('12345', '123456', None)
        print paquete
        self.assertTrue(isinstance(paquete, Paquete))

    def test_paquete_len_codpaq_gt_5(self):
        """
        Test para la creación de un paquete
        con un len(codpaq)>5
        """
        # -------------------------------------------
        # Len(cod_paq) > 5
        paquete = self.crear_paquete('123456', None, None)
        self.assertFalse(isinstance(paquete, Paquete))

    def test_paquete_codpaq_null(self):
        """
        Test para la creación de un paquete
        con un len(codpaq)>5
        """
        # -------------------------------------------
        # Len(cod_paq) > 5
        paquete = self.crear_paquete(None, '123456', None)
        self.assertFalse(isinstance(paquete, Paquete))
