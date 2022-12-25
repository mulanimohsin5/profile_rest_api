from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class HelloApiView(APIView):
    """ Test Api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return List off api view features"""
        an_api_view = [
            "Uses HTTP methods as a functions (GET,POST,PUT,PATCH,DESTOY)",
            "It is similar to the traditional django views",
            "Give most control over your logic",
            "it mapped manually to URLs"
        ]
        return Response({'message': f"Hello!@ {self.request.user.name}", 'an_api_view': an_api_view})

    def post(self, request):
        """
        Create a hello message with logged in user name.
        """
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int = None):
        """
        Handle updating an object.
        """
        return Response({'Method': "put"})

    def patch(self, request, pk: int = None):
        """
        - Handle partial updating  of object.
        - Update only fields those are sent in request.
        """
        return Response({'Method': "patch"})

    def delete(self, request, pk: int = None):
        """
        - delete an object
        """
        return Response({'Method': "delete"})
