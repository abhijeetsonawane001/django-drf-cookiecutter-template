from split_settings.tools import include

from {{cookiecutter.project_slug}}.settings.components.environ import env

_DJANGO_ENV = env("DJANGO_ENV")

_base_settings = (
    "components/common.py",
    "components/logging.py",
    "components/api_apps.py",
    "components/mail.py",
    # env
    "environments/{0}.py".format(_DJANGO_ENV),
)
# Include Settings
include(*_base_settings)