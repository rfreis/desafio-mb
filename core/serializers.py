from rest_framework.serializers import (
    ModelSerializer,
)

from district.serializers import DistrictSerializer

from .models import Fair


class FairSerializer(ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = Fair
        fields = [
            "id",
            "district",
            "name",
            "longitude",
            "latitude",
            "setcens",
            "area",
            "register",
            "street",
            "number",
            "neighborhood",
            "reference",
        ]


class FairUpdateSerializer(ModelSerializer):
    class Meta:
        model = Fair
        fields = [
            "id",
            "district",
            "name",
            "longitude",
            "latitude",
            "setcens",
            "area",
            "register",
            "street",
            "number",
            "neighborhood",
            "reference",
        ]
