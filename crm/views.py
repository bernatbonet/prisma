"""
CRM views
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Modules
from .serializers import ModuleSerializer

class ModulesApiView(APIView):
    """
    List all the modules when the GET method is called
    Add new module when the POST method is called
    Delete a module when the DELETE method is called
    """

    def get(self, request, format=None):
        """
        Return a list of all the modules object in the database
        """
        # query the database for all instances of the Modules model
        modules = Modules.objects.all()

        # serialize the data into a returnable format
        serializer = ModuleSerializer(modules, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Creates a new module with the given data
        """
        # deserialize the data from the request
        serializer = ModuleSerializer(data=request.data)

        # if the data validation done by the serializer passes
        if serializer.is_valid():
            # then save the module to the database and return the resulting module
            serializer.save()
            return Response(serializer.data)
        else:
            # Throw a 400 error if the serializer detected the data wasm't valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, module_id, format=None):
        """
        Deletes a module from the database
        """
        # do this in a try block to catch errors if the module isn't real
        try:
            # if the module is real the delete
            module = Modules.objects.get(id=module_id)
            module.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # catch the DoesNotExist error and return an Http error
        except Modules.DoesNotExist:
            raise Http404
