# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from crm.serializers import ModuleSerializer


class ModulesTestCase(TestCase):
    """
    Test for modules serializer
    """

    def test_module_create(self):
        """
        Define some json data we expect to receive and use the
        serializer to parse it into the models. Test the models
        to make sure they're correct
        """
        data = {
            'mod_apl': 'CNF',
            'mod_codigo': 'MOD',
            'mod_desc': 'Modules',
            'mod_version': '0,0'
        }
        # pass the data into the serializer to try to parse it
        serializer = ModuleSerializer(data=data)

        # verify that the serializer thinks the data is valid
        self.assertTrue(serializer.is_valid())

        # get the object parsed from the serializer
        module = serializer.save()

        # verify the mod_desc is correct
        self.assertEqual(module.mod_desc, 'Modules')
