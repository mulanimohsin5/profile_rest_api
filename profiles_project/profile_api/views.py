from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import UserProfile
from .serializers import UserProfileSerializer


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
        return Response({'message': f"Hello!@ {self.request.user.name}",
                         'an_api_view': an_api_view})

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


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    def list(self, request):
        """Return Hello message."""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update',
            'automatically maps to url using routers',
            'provides more functionality with less code.'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def post(self, request):
        """Create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_request": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_request": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_request": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle remove an object"""
        return Response({"http_request": "DELETE"})

class UserProfileViewset(viewsets.ModelViewSet):
    """ handles creating and updating profiles."""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.object.all()