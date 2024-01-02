from drf_yasg import openapi

from api.v1.serializers.photo.create import CreatePhotoSerializer
from api.v1.serializers.photo.list import ListPhotoSerializer
from api.v1.serializers.photo.show import PhotoSerializer

CREATE_PHOTO_DOC = {
    "tags": ["photo"],
    "operation_id": "Photo create",
    "operation_description": "Create new photo",
    "request_body": CreatePhotoSerializer,
    "responses": {200: openapi.Response("Success", PhotoSerializer(many=True))},
}

SHOW_PHOTO_DOC = {
    "tags": ["photo"],
    "operation_id": "Photo",
    "operation_description": "Show photo",
    "responses": {200: openapi.Response("Success", PhotoSerializer)}
}

LIST_PHOTO_DOC = {
    "tags": ["photo"],
    "operation_id": "Photo list",
    "operation_description": "Get photo list",
    "manual_parameters": [
        openapi.Parameter(
            name="page",
            in_=openapi.IN_QUERY,
            description="Page number",
            type=openapi.TYPE_INTEGER,
        ),
        openapi.Parameter(
            name="per_page",
            in_=openapi.IN_QUERY,
            description="Page size",
            type=openapi.TYPE_INTEGER,
        ),
    ],
    "responses": {200: openapi.Response("Success", ListPhotoSerializer(many=True))},
}
