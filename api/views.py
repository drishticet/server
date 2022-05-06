from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from user import models
from user import serializers

class LeaderBoard(generics.ListAPIView):
    username = None
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        response.data = response.data[:5]
        return super().finalize_response(request, response, *args, **kwargs)

class UsernameListView(APIView):
    username = None
    def get(self, request, format=None):
        a = [f.username for f in models.CustomUser.objects.all()]
        context = {
            "users" : a
        }
        return Response(context)
