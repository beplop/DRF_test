from rest_framework import viewsets
from rest_framework.response import Response

from .models import Letters, Packages
from .serializers import LettersSerializer, PackagesSerializer


class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letters.objects.all()
    serializer_class = LettersSerializer


# class PackagesViewSet(viewsets.ModelViewSet):
#     queryset = Packages.objects.all()
#     serializer_class = PackagesSerializer

class PackagesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Packages.objects.all()
        return Response(PackagesSerializer(queryset, many=True).data)

    def create(self, request):
        serializer = PackagesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if not pk:
            return Response({"error": "Method Retrieve not allowed"})

        try:
            queryset = Packages.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        return Response(PackagesSerializer(queryset).data)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Update not allowed"})

        try:
            instance = Packages.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = PackagesSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Destroy not allowed"})

        try:
            instance = Packages.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response("delete post " + str(pk))
