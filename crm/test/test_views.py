# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.test import Client
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from core.models import User
from crm.models import Modules


class UserTestCase(TestCase):
    """
    Test for user views
    """
    def setUp(self):
        """Initialize the TestCase with APiClient"""
        self.client = APIClient()
        self.user = User.objects.create('test', 'test123', 'test@test.es')
        self.token = Token.objects.create(user = self.user)

    def test_login(self):
        """
        Tests the login module
        """
        
        self.client.force_login(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + token.key)
    
        # define the data to post
        post_data = {
            'mod_apl': 'CNF',
            'mod_codigo': 'ROL',
            'mod_desc': 'Roles',
            'mod_version': '0,0'
        }

        # post a new module
        response = self.client.post(
            '/crm/modules',
            json.dumps(post_data),
            content_type='application/json'
        )

        # always assert that your status code is what you expect
        self.assertEqual(response.status_code, 200)
        

class ModulesTestCase(TestCase):
    """
    Test for modules views
    """

    def setUp(self):
        """Initialize the TestCase with a test client"""
        self.client = Client()
        self.modules = Modules.objects.create(mod_apl="CNF",
                                              mod_codigo="MOD",
                                              mod_desc="Modules",
                                              mod_version="0.1")
        super(ModulesTestCase, self).setUp()

    def test_modules_post_delete(self):
        """
        Tests the modules POST method to add items
        and the modules DELETE method to revome modules
        """
        # define the data to post
        post_data = {
            'mod_apl': 'CNF',
            'mod_codigo': 'ROL',
            'mod_desc': 'Roles',
            'mod_version': '0,0'
        }

        # post a new module
        response = self.client.post(
            '/crm/modules',
            json.dumps(post_data),
            content_type='application/json'
        )

        # always assert that your status code is what you expect
        self.assertEqual(response.status_code, 200)


        # get the module id from the response
        module_id = response.data['id']

        # now retrieve all the modules
        response = self.client.get(
            '/crm/modules'
        )
        self.assertEqual(response.status_code, 200)

        # get the modules list from the endpoint
        received_modules = response.data

        # search for the module we posted
        is_present = False
        for module_item in received_modules:
            if module_item['id'] == module_id:
                is_present = True
                break

        # assert that the item we posted was indeed found
        self.assertTrue(is_present)

        # delete the created module
        response = self.client.delete(
            '/crm/modules/{0}'.format(module_id)
        )

        # verify we get a 204 HTTP No Content Response
        self.assertEqual(response.status_code, 204)
