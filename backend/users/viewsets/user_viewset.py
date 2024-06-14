from typing import ClassVar

from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import GenericViewSet

from ..serializers import UserSerializer


@extend_schema(tags=["User"])
class UserViewSet(GenericViewSet):
    """API для взаимодействия с личным кабинетом."""

    permission_classes: ClassVar[list[type[BasePermission]]] = [AllowAny]

    def get_serializer_class(self) -> type[BaseSerializer]:
        return UserSerializer

    def list(self, request: Request) -> Response:
        if not bool(request.user and request.user.is_authenticated):
            return Response({"ok": False, "errors": "not authorized"})
        serializer: UserSerializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)

    def retrieve(self, request: Request) -> Response:
        if not bool(request.user and request.user.is_authenticated):
            return Response({"ok": False, "errors": "not authorized"})

        serializer: UserSerializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)
