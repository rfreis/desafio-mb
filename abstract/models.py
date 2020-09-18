from django.db import models


class Name(models.Model):
    """
    Abstract model with name.
    """
    name = models.CharField(max_length=255, verbose_name="Nome")

    class Meta:
        abstract = True
