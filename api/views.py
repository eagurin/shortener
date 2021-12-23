from django.shortcuts import get_object_or_404, redirect
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Url
from .serializers import UrlSerializer


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            {"shorten": request.build_absolute_uri(instance.get_short_url())},
            status=status.HTTP_201_CREATED,
        )


def root(request, shorten):
    data = get_object_or_404(Url, shorten=shorten)
    data.clicked()
    return redirect(data.url)
