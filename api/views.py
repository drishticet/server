from rest_framework import generics
from rest_framework.response import Response

from user import models
from user import serializers

class LeaderBoard(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data = response.data[:5]
        return super().finalize_response(request, response, *args, **kwargs)
