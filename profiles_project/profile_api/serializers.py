from rest_framework import serializers

from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    """
    Hello serializer  for api
    """

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name')
