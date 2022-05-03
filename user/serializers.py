from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_auth.registration.serializers import RegisterSerializer

import random
import string

class UserSerializer(RegisterSerializer):
    college_name = serializers.CharField(required=True,max_length=100)
    name = serializers.CharField(required=True,max_length=100)
    phonenumber = serializers.CharField(required=True,max_length=100)
    referral_code = serializers.CharField(max_length=7, read_only=True)
    points = serializers.IntegerField(default=0, read_only=True)

    def get_cleaned_data(self):
        # data_dict = super(UserSerializer(), self).get_cleaned_data()
        data_dict = super().get_cleaned_data()
        data_dict['college_name'] = self.validated_data.get('college_name', '')
        data_dict['name'] = self.validated_data.get('name', '')
        data_dict['phonenumber'] = self.validated_data.get('phonenumber', '')
        data_dict['referral_code'] = self.validated_data.get('referral_code', '')

        print('validated referal code ', self.validated_data.get('referral_code', ''))
        
        return data_dict

    def save(self, request):
        user = super().save(request)
        user.college_name = self.data.get('college_name')
        user.name = self.data.get('name')
        user.phonenumber = self.data.get('phonenumber')
        user.points = 0

        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
        user.referral_code = res

        print('Refereal code : ', res)

        user.save()
        return user
