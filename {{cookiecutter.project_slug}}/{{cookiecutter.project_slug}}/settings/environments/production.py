from {{cookiecutter.project_slug}}.settings.components.environ import env

DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": env.db()}