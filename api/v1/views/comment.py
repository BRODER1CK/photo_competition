from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.v1.docs.comment import LIST_COMMENT_DOC, CREATE_COMMENT_DOC, UPDATE_COMMENT_DOC, DELETE_COMMENT_DOC
from api.v1.serializers.comment.create import CreateCommentSerializer
from api.v1.serializers.comment.list import ListCommentSerializer
from api.v1.services.comment.create import CommentCreateService
from api.v1.services.comment.delete import CommentDeleteService
from api.v1.services.comment.list import CommentListService
from api.v1.services.comment.update import CommentUpdateService


class ListCommentView(APIView):
    serializer_class = ListCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(**LIST_COMMENT_DOC)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentListService, request.GET.dict())
        return Response(
            {
                "results": ListCommentSerializer(
                    outcome.result.object_list, many=True
                ).data,
            }
        )


class CreateCommentView(APIView):
    serializer_class = CreateCommentSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**CREATE_COMMENT_DOC)
    def post(self, request: Request, *args, **kwargs):
        outcome = ServiceOutcome(CommentCreateService,
                                 request.POST.dict() | {'current_user': request.user})
        return Response(ListCommentSerializer(outcome.result).data, status=status.HTTP_200_OK)


class UpdateDeleteCommentView(APIView):
    serializer_class = ListCommentSerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(**UPDATE_COMMENT_DOC)
    def put(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        outcome = ServiceOutcome(CommentUpdateService, request.data.dict() | kwargs | {'current_user': user})
        return Response(ListCommentSerializer(outcome.result).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(**DELETE_COMMENT_DOC)
    def delete(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user
        ServiceOutcome(CommentDeleteService, kwargs | {'current_user': user})
        return Response(None, status=status.HTTP_200_OK)
