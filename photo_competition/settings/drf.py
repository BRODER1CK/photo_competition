from decouple import config

REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 9,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "EXCEPTION_HANDLER": "utils.exception_handler.drf_exception_response",
}

SWAGGER_SETTINGS = {
    "LOGIN_URL": f'{config("SCHEMA")}://{config("DOMAIN")}/social-auth/login/vk-oauth2/',
    "LOGOUT_URL": f'{config("SCHEMA")}://{config("DOMAIN")}/logout/',
    "SECURITY_DEFINITIONS": {
        "Token": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
}

CORS_ALLOW_ALL_ORIGINS = True
