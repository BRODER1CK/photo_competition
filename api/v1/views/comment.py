from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.v1.docs.comment import (CREATE_COMMENT_DOC, DELETE_COMMENT_DOC,
                                 LIST_COMMENT_DOC, SHOW_COMMENT_DOC,
                                 UPDATE_COMMENT_DOC)
from api.v1.permissions.has_token_or_read_only import HasTokenOrReadOnly
from api.v1.serializers.comment.list import ListCommentSerializer
from api.v1.serializers.comment.show import ShowCommentSerializer
from api.v1.services.comment.create import CommentCreateService
from api.v1.services.comment.delete import CommentDeleteService
from api.v1.services.comment.list import CommentListService
from api.v1.services.comment.show import CommentShowService
from api.v1.services.comment.update import CommentUpdateService


class ListCreateCommentView(APIView):
    permission_classes = [HasTokenOrReadOnly]

    @swagger_auto_schema(**LIST_COMMENT_DOC)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentListService, request.GET.dict())
        return Response(
            ListCommentSerializer(outcome.result, many=True).data,
            status=outcome.response_status,
        )

    @swagger_auto_schema(**CREATE_COMMENT_DOC)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            CommentCreateService, request.data | kwargs | {"current_user": request.user}
        )
        return Response(
            ListCommentSerializer(outcome.result).data, status=status.HTTP_201_CREATED
        )


class UpdateDeleteCommentView(APIView):
    permission_classes = [HasTokenOrReadOnly]

    @swagger_auto_schema(**SHOW_COMMENT_DOC)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            CommentShowService, kwargs | {"current_user": request.user}
        )
        return Response(
            ShowCommentSerializer(outcome.result).data, status=outcome.response_status
        )

    @swagger_auto_schema(**UPDATE_COMMENT_DOC)
    def put(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            CommentUpdateService, request.data | kwargs | {"current_user": request.user}
        )
        return Response(
            ListCommentSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @swagger_auto_schema(**UPDATE_COMMENT_DOC)
    def patch(self, request, *args, **kwargs):
        return self.put(request, args, kwargs)

    @swagger_auto_schema(**DELETE_COMMENT_DOC)
    def delete(self, request, *args, **kwargs):
        ServiceOutcome(CommentDeleteService, kwargs | {"current_user": request.user})
        return Response(None, status=status.HTTP_200_OK)
