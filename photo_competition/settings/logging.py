LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"request_id": {"()": "log_request_id.filters.RequestIDFilter"}},
    "formatters": {
        "standard": {
            "format": "%(levelname)-8s [%(asctime)s] [%(request_id)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "rich.logging.RichHandler",
            "filters": ["request_id"],
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "db.log",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
