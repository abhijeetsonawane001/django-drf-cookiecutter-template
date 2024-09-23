import os

from {{cookiecutter.project_slug}}.settings.components.environ import BASE_DIR, env

# Ensure the logs directory exists
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {funcName} {lineno} {message}",  # noqa E501
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join("logs", "{{cookiecutter.project_slug}}_app.log"),
            "maxBytes": 5 * 1024 * 1024,  # 5 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
        "console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

if env("DJANGO_ENV") == "production":
    LOGGING["handlers"]["console"]["level"] = "ERROR"
    LOGGING["loggers"][""]["level"] = "INFO"
elif env("DJANGO_ENV") == "development":
    LOGGING["handlers"]["console"]["level"] = "DEBUG"
    LOGGING["loggers"][""]["level"] = "DEBUG"