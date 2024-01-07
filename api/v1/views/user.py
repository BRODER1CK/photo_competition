from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.v1.docs.user import UPDATE_USER_DOC, SHOW_USER_DOC, PARTIAL_UPDATE_USER_DOC
from api.v1.services.user.show import UserShowService
from api.v1.services.user.update import UserUpdateService, UserPartialUpdateService
from api.v1.serializers.user.show import UserSerializer


class RetrieveUpdateUserView(APIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**SHOW_USER_DOC)
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(UserShowService, kwargs | {'current_user': user})
        return Response(UserSerializer(outcome.result).data, status=outcome.response_status)

    @swagger_auto_schema(**UPDATE_USER_DOC)
    def put(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(UserUpdateService, request.data.dict() | kwargs | {'current_user': user})
        return Response(UserSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**PARTIAL_UPDATE_USER_DOC)
    def patch(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(UserPartialUpdateService, request.data.dict() | kwargs | {'current_user': user})
        return Response(UserSerializer(outcome.result).data, status=status.HTTP_200_OK)
