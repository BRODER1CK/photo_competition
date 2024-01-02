REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    "EXCEPTION_HANDLER": "utils.exception_handler.drf_exception_response",
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'http://127.0.0.1:8000/social-auth/login/vk-oauth2/',
    'LOGOUT_URL': 'http://127.0.0.1:8000/logout/',
}
