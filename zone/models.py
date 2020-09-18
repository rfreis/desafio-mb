from django.db import models

from abstract.models import Name


class Zone5(Name):
    """
    This model stores data about 'REGIAO5' in SP
    """

    class Meta:
        verbose_name = "REGIÃO 5"
        verbose_name_plural = "REGIÕES 5"

    def __str__(self):
        return "{id}. {name}".format(id=self.id, name=self.name)


class Zone8(Name):
    """
    This model stores data about 'REGIAO8' in SP
    """
    zone_5 = models.ForeignKey(
        Zone5, related_name="zone_8", on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "REGIÃO 8"
        verbose_name_plural = "REGIÕES 8"

    def __str__(self):
        return "{id}. {zone_8} ({zone_5})".format(
            id=self.id, zone_8=self.name, zone_5=self.zone_5
        )
