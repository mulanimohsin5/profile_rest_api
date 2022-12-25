from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """
    Hello serializer  for api
    """

    name = serializers.CharField(max_length=10)
