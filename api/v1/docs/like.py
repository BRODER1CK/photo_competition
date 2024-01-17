from drf_yasg import openapi


from api.v1.serializers.like.list import ListLikeSerializer
from api.v1.serializers.like.show import ShowLikeSerializer

CREATE_LIKE_DOC = {
    "tags": ["like"],
    "operation_id": "Like create",
    "operation_description": "Create like",
    "responses": {200: openapi.Response("Success", ShowLikeSerializer)}
}

DELETE_LIKE_DOC = {
    "tags": ["like"],
    "operation_id": "Like delete",
    "operation_description": "Delete like",
    "responses": {200: openapi.Response("Success", None)}
}

LIST_LIKE_DOC = {
    "tags": ["like"],
    "operation_id": "Like list",
    "operation_description": "Get like list",
    "manual_parameters": [
        openapi.Parameter(
            name="photo_id",
            in_=openapi.IN_QUERY,
            description="Photo id",
            type=openapi.TYPE_INTEGER,
        ),
    ],
    "responses": {200: openapi.Response("Success", ListLikeSerializer(many=True))}
}
