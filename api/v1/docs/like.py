from drf_yasg import openapi


from api.v1.serializers.like.createdelete import CreateDeleteLikeSerializer
from api.v1.serializers.like.list import ListLikeSerializer

CREATE_DELETE_LIKE_DOC = {
    "tags": ["like"],
    "operation_id": "Like create/delete",
    "operation_description": "Create/delete like",
    "responses": {200: openapi.Response("Success", CreateDeleteLikeSerializer)}
}

LIST_LIKE_DOC = {
    "tags": ["like"],
    "operation_id": "Like list",
    "operation_description": "Get like list",
    "responses": {200: openapi.Response("Success", ListLikeSerializer)}
}
