from rest_framework.serializers import (
    ModelSerializer,
)

from zone.serializers import Zone8Serializer

from .models import SubPrefecture


class SubPrefectureSerializer(ModelSerializer):
    zone_8 = Zone8Serializer()

    class Meta:
        model = SubPrefecture
        fields = [
            "id",
            "name",
            "zone_8",
        ]
