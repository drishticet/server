from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from .models import CustomUser

import random
import string

class UserSerializer(RegisterSerializer):
    username = None
    college_name = serializers.CharField(required=True,max_length=100)
    name = serializers.CharField(required=True,max_length=100)
    phonenumber = serializers.CharField(required=True,max_length=100)
    referral_code = serializers.CharField(max_length=7, read_only=True)
    points = serializers.IntegerField(default=0, read_only=True)

    ordering = ('email',)

    def get_cleaned_data(self):
        # data_dict = super(UserSerializer(), self).get_cleaned_data()
        data_dict = super().get_cleaned_data()
        data_dict['college_name'] = self.validated_data.get('college_name', '')
        data_dict['name'] = self.validated_data.get('name', '')
        data_dict['phonenumber'] = self.validated_data.get('phonenumber', '')
        data_dict['referral_code'] = self.validated_data.get('referral_code', '')        
        return data_dict

    def save(self, request):
        # for getting unique referral code
        while True:
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
            if not CustomUser.objects.filter(referral_code=res).exists():
                break

        user = super().save(request)
        user.college_name = self.data.get('college_name')
        user.name = self.data.get('name')
        user.phonenumber = self.data.get('phonenumber')
        user.points = 0
        user.referral_code = res
        user.save()
        return user
