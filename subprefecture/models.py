from django.db import models

from zone.models import Zone8

from abstract.models import Name


class SubPrefecture(Name):
    """
    This model stores data about 'SUBPREFE' in SP
    """
    zone_8 = models.ForeignKey(
        Zone8, related_name="sub_prefecture", on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "SUB PREFEITURA"
        verbose_name_plural = "SUB PREFEITURAS"

    def __str__(self):
        return "{id}. {name}".format(id=self.id, name=self.name)
