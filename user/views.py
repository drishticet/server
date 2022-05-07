from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

# class UserView(generics.RetrieveAPIView):
    # lookup_field = 'email'
    # queryset = models.CustomUser.objects.all()
    # serializer_class = serializers.UserSerializer

class UserView(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self, request, format=None):
        user = request.user
        if user.id:
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"error":"need to be logged in"})
