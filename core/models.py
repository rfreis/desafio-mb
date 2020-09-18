from django.db import models

from abstract.models import Name
from district.models import District


class Fair(Name):
    """
    This model stores data about street fair in SP
    """

    district = models.ForeignKey(
        District,
        related_name="fair",
        on_delete=models.PROTECT,
        verbose_name="DISTRITO",
    )
    longitude = models.DecimalField(
        max_digits=20, decimal_places=6, verbose_name="LONG"
    )
    latitude = models.DecimalField(
        max_digits=20, decimal_places=6, verbose_name="LAT"
    )
    setcens = models.CharField(
        max_length=255,
        verbose_name="SETCENS",
    )
    area = models.CharField(
        max_length=255,
        verbose_name="AREAP",
    )
    register = models.CharField(max_length=255, verbose_name="REGISTRO")
    street = models.CharField(max_length=255, verbose_name="LOGRADOURO")
    number = models.CharField(
        max_length=255, verbose_name="NÚMERO", blank=True, null=True
    )
    neighborhood = models.CharField(
        max_length=255, verbose_name="BAIRRO", blank=True, null=True
    )
    reference = models.CharField(
        max_length=255, verbose_name="REFERENCIA", blank=True, null=True
    )

    class Meta:
        verbose_name = "FEIRA"
        verbose_name_plural = "FEIRAS"

    def __str__(self):
        return "{id}. {name}".format(id=self.id, name=self.name)
