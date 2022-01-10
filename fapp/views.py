# from django.shortcuts import render, resolve_url
# from rest_framework import serializers
# from rest_framework import response
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .models import Notes, NotesSerializer
# from rest_framework import status
# from django.http import Http404
# from rest_framework import mixins, generics
# Create your views here.

# viewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication
# Create your views here.


class WritebyAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False

class NotesViewSet(ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, WritebyAdminOnlyPermission]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer