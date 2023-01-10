from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from .views import HelloApiView, HelloViewSet, UserProfileViewset

router = DefaultRouter()
router.register('hello_viewset', HelloViewSet, basename='hello_viewset')
router.register('profile',UserProfileViewset,basename='profile')
urlpatterns = [

    path("", include(router.urls)),
    path('hello-view/', HelloApiView.as_view())
]
