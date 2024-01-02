from split_settings.tools import include


settings = ['base.py', 'authentication.py', 'drf.py']
include(
    *settings
)