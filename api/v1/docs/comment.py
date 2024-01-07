from drf_yasg import openapi

from api.v1.serializers.comment.create import CreateCommentSerializer
from api.v1.serializers.comment.list import ListCommentSerializer
from api.v1.serializers.comment.update import UpdateCommentSerializer

CREATE_COMMENT_DOC = {
    "tags": ["comment"],
    "operation_id": "Comment create",
    "operation_description": "Create new comment",
    "request_body": CreateCommentSerializer,
    "responses": {200: openapi.Response("Success", ListCommentSerializer(many=True))},
}

UPDATE_COMMENT_DOC = {
    "tags": ["comment"],
    "operation_id": "Comment update",
    "operation_description": "Update comment",
    "request_body": UpdateCommentSerializer,
    "responses": {200: openapi.Response("Success", ListCommentSerializer(many=True))},
}

LIST_COMMENT_DOC = {
    "tags": ["comment"],
    "operation_id": "Comment list",
    "operation_description": "Get comment list",
    "responses": {200: openapi.Response("Success", ListCommentSerializer(many=True))},
}

DELETE_COMMENT_DOC = {
    "tags": ["comment"],
    "operation_id": "Comment delete",
    "operation_description": "Delete comment",
    "responses": {200: openapi.Response("Success", ListCommentSerializer)}
}
