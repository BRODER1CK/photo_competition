from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.v1.docs.like import LIST_LIKE_DOC, DELETE_LIKE_DOC, CREATE_LIKE_DOC

from api.v1.serializers.like.list import ListLikeSerializer
from api.v1.services.like.create import LikeCreateService

from api.v1.services.like.delete import LikeDeleteService
from api.v1.services.like.list import LikeListService


class ListLikeView(APIView):
    serializer_class = ListLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**LIST_LIKE_DOC)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(LikeListService, request.GET.dict())
        return Response(ListLikeSerializer(outcome.result, many=True).data, status=outcome.response_status)


class CreateDeleteLikeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**CREATE_LIKE_DOC)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(LikeCreateService, request.data | kwargs | {'current_user': request.user})
        return Response(ListLikeSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**DELETE_LIKE_DOC)
    def delete(self, request, *args, **kwargs):
        ServiceOutcome(LikeDeleteService, kwargs | {'current_user': request.user})
        return Response(None, status=status.HTTP_200_OK)
