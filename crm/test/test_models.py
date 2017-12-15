# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from crm.models import Modules


class ModulesTestCase(TestCase):
    """
    Test for Modules model
    """

    def test_modules(self):
        """
        Test creating a module
        """
        # create a module object (this saves it to database)
        Modules.objects.create(mod_apl="CNF",
                               mod_codigo="MOD",
                               mod_desc="Modules",
                               mod_version="0.1")
        # verify the objects was found
        module = Modules.objects.get(mod_apl="CNF", mod_codigo="MOD")
        # verify the data is accurate and exits
        self.assertEqual(module.mod_desc, "Modules")
        # delete the module
        module.delete()
        # try to retrieve the module and make sure it's not there
        try:
            retrieved_module = Modules.objects.get(
                mod_apl="CNF", mod_codigo="MOD")
        except Modules.DoesNotExist:
            retrieved_module = None
        self.assertEqual(retrieved_module, None)
