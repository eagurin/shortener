from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UrlViewSet, root

router = DefaultRouter(trailing_slash=False)
router.register("_short", UrlViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<str:shorten>", root, name="root"),
]
