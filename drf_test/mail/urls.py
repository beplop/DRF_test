from django.urls import include, re_path, path
from .views import LettersViewSet, PackagesViewSet
from rest_framework import routers

letters_router = routers.SimpleRouter()
letters_router.register(r'letter', LettersViewSet, basename='Letters')

packages_router = routers.SimpleRouter()
packages_router.register(r'package', PackagesViewSet, basename='Packages')

urlpatterns = [
    path("", include(packages_router.urls)),
    path("", include(letters_router.urls)),
]
