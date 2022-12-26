from rest_framework.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet

router=DefaultRouter()
router.register('hello_viewset',HelloViewSet,basename='hello_viewset')
urlpatterns = [
    path("",include(router.urls)),
    path('hello-view/', HelloApiView.as_view()),   
 ]

