from {{cookiecutter.project_slug}}.settings.components.environ import env

DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": env.db()}


# COOKIE, CSRF, CORS Config
# COOKIE
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"  # or 'Strict'


# CSRF
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "Lax"  # or 'Strict'
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS", list, ["http://localhost:3000"])  # noqa E501