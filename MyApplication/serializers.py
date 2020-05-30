from rest_framework import serializers
from MyApplication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('age', 'job', 'file')


# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = fileModel
#         fields = ('userId', 'file')
