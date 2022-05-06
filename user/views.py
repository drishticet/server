from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserView(generics.RetrieveAPIView):
    # lookup_field = 'username'
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
