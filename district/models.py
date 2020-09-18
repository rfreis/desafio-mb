from django.db import models

from subprefecture.models import SubPrefecture

from abstract.models import Name


class District(Name):
    """
    This model stores data about 'DISTRITO' in SP
    """
    sub_prefecture = models.ForeignKey(
        SubPrefecture, related_name="district", on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "DISTRITO"
        verbose_name_plural = "DISTRITOS"

    def __str__(self):
        return "{id}. {name}".format(id=self.id, name=self.name)
