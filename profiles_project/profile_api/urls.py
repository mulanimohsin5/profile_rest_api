from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from .views import HelloApiView, HelloViewSet, UserProfileViewSet, LoginViewSet

router = DefaultRouter()
router.register('hello_viewset', HelloViewSet, basename='hello_viewset')
router.register('profile', UserProfileViewSet, basename='user_profile')
router.register('login', LoginViewSet, basename='login')
urlpatterns = [

    path("", include(router.urls)),
    path('hello-view/', HelloApiView.as_view())
]
