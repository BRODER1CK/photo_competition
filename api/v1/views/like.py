from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.v1.docs.like import CREATE_DELETE_LIKE_DOC, LIST_LIKE_DOC

from api.v1.serializers.like.createdelete import CreateDeleteLikeSerializer
from api.v1.serializers.like.list import ListLikeSerializer
from api.v1.services.like.createdelete import CreateDeleteLikeService
from api.v1.services.like.list import LikeListService


class ListLikeView(APIView):
    serializer_class = ListLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(**LIST_LIKE_DOC)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(LikeListService, kwargs)
        return Response(ListLikeSerializer(outcome.result).data, status=outcome.response_status)


class CreateDeleteLikeView(APIView):
    serializer_class = CreateDeleteLikeSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**CREATE_DELETE_LIKE_DOC)
    def post(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(CreateDeleteLikeService, request.data | kwargs | {'current_user': user})
        return Response(ListLikeSerializer(outcome.result).data, status=status.HTTP_200_OK)
