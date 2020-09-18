from rest_framework.serializers import (
    ModelSerializer,
)

from subprefecture.serializers import SubPrefectureSerializer

from .models import District


class DistrictSerializer(ModelSerializer):
    sub_prefecture = SubPrefectureSerializer()

    class Meta:
        model = District
        fields = [
            "id",
            "name",
            "sub_prefecture",
        ]
