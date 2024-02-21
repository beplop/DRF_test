from django.urls import include, path
from .views import LettersViewSet, PackagesViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'letter', LettersViewSet, basename='letters')
router.register(r'package', PackagesViewSet, basename='packages')

urlpatterns = [
    path('', include(router.urls)),
]
