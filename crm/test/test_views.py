# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase, Client
from django.test import Client
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from core.models import User
from crm.models import Modules

class ModulesTestCase(TestCase):
    """
    Test for modules views
    """

    def setUp(self):
        """Initialize the TestCase with a test client"""
        self.client = APIClient()
        self.user = User.objects.create(
            username='test',
            email='test@test.es',
            password='test123')
        self.token = Token.objects.get(user = self.user)

    def test_modules_post_get_delete(self):
        """
        Tests the modules POST method to add items
        and the modules DELETE method to revome modules
        """
        # check post with no credentials
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
        #   401 - Unauthorized
        self.assertEqual(response.status_code, 401)

        # get method for unauthenticated users
        response = self.client.get(
            '/crm/modules/{0}'.format(response.data['id'])
        )
        print reponse.data['mod_codigo']
        self.assertEqual(response.status_code, 200)

        # ------------------------------------------------------

        # ckeck post with credentials 
        # user credentials
        self.client.force_login(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key)

        # define the data to post
        post_data = [{
            'mod_apl': 'CNF',
            'mod_codigo': 'MOD',
            'mod_desc': 'Modules',
            'mod_version': '0,0'
        },{
            'mod_apl': 'CNF',
            'mod_codigo': 'ROL',
            'mod_desc': 'Roles',
            'mod_version': '0,0'
        },{
            'mod_apl': 'CNF',
            'mod_codigo': 'USR',
            'mod_desc': 'Users',
            'mod_version': '0,0'
        }]

        # post a new module
        for item in post_data:
            response = self.client.post(
                '/crm/modules',
                json.dumps(item),
                content_type='application/json'
            )
           
            # always assert that your status code is what you expect
            #   200 - OK
            self.assertEqual(response.status_code, 200)

            # get the module id from the response
            module_id = response.data['id']

            # now retrieve all the modules
            response = self.client.get(
                '/crm/modules/{0}'.format(module_id)
            )
            self.assertEqual(response.status_code, 200)

        # now retrieve all the modules
        response = self.client.get(
            '/crm/modules'
        )

        # get the modules list from the endpoint
        received_modules = response.data

        # search for the last module we posted
        is_present = False
        for module_item in received_modules:
            if module_item['id'] == module_id:
                is_present = True
                break

        # assert that the item we posted was indeed found
        self.assertTrue(is_present)

        # delete the created module
        for item in received_modules:
            response = self.client.delete(
                '/crm/modules/{0}'.format(item['id'])
            )

            # verify we get a 204 HTTP No Content Response
            self.assertEqual(response.status_code, 204)
