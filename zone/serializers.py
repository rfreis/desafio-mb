from rest_framework.serializers import (
    ModelSerializer,
)

from .models import Zone5, Zone8


class Zone5Serializer(ModelSerializer):
    class Meta:
        model = Zone5
        fields = [
            "id",
            "name",
        ]


class Zone8Serializer(ModelSerializer):
    zone_5 = Zone5Serializer()

    class Meta:
        model = Zone8
        fields = [
            "id",
            "name",
            "zone_5",
        ]
