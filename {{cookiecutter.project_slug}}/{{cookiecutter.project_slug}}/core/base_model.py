from django.db import models
from nanoid import generate


def generate_nanoid():
    return generate(size=21)


class BaseModel(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=50,
        editable=False,
        unique=True,
        default=generate_nanoid,  # noqa E501
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True