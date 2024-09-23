import os
from pathlib import Path

import environ

env = environ.Env(
    DJANGO_ENV=(str, "development"),
    ALLOWED_HOSTS=(list, "localhost,127.0.0.1"),
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))