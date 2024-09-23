from {{cookiecutter.project_slug}}.settings.components.environ import env

# SMTP Provider
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="no-reply@yourdomain.com")
EMAIL_HOST = env("EMAIL_HOST", default="maildev")
EMAIL_PORT = env("EMAIL_PORT", default=1025)

if env("DJANGO_ENV") == "production":
    EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=False)
    EMAIL_USE_SSL = env("EMAIL_USE_SSL", default=False)