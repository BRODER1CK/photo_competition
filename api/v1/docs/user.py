from drf_yasg import openapi

from api.v1.serializers.user.generate_token import GenerateTokenSerializer
from api.v1.serializers.user.show import UserSerializer
from api.v1.serializers.user.update import (
    PartialUpdateUserSerializer,
    UpdateUserSerializer,
)

UPDATE_USER_DOC = {
    "tags": ["user"],
    "operation_id": "User update",
    "operation_description": "Update user",
    "request_body": UpdateUserSerializer,
    "responses": {200: openapi.Response("Success", UserSerializer(many=True))},
}

PARTIAL_UPDATE_USER_DOC = {
    "tags": ["user"],
    "operation_id": "User partial update",
    "operation_description": "Partial update user",
    "request_body": PartialUpdateUserSerializer,
    "responses": {200: openapi.Response("Success", UserSerializer(many=True))},
}

SHOW_USER_DOC = {
    "tags": ["user"],
    "operation_id": "User show",
    "operation_description": "Show user",
    "responses": {200: openapi.Response("Success", UserSerializer)},
}

GENERATE_TOKEN_DOC = {
    "tags": ["user"],
    "operation_id": "Token generate",
    "operation_description": "Generate token",
    "responses": {200: openapi.Response("Success", GenerateTokenSerializer)},
}
