from decouple import config

from photo_competition.settings.base import MEDIA_URL

AUTH_USER_MODEL = "models_app.User"

AUTHENTICATION_BACKENDS = [
    "social_core.backends.vk.VKOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "web_site:profile"

DEFAULT_USER_IMAGE = MEDIA_URL + "web_site/default.png"

SOCIAL_AUTH_VK_OAUTH2_KEY = config("SOCIAL_AUTH_VK_OAUTH2_KEY")
SOCIAL_AUTH_VK_OAUTH2_SECRET = config("SOCIAL_AUTH_VK_OAUTH2_SECRET")
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["photos", "email"]
SOCIAL_AUTH_URL_NAMESPACE = "social"

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
    "models_app.pipelines.pipeline.get_avatar",
    "models_app.pipelines.pipeline.get_email",
)
