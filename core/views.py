from django.shortcuts import (
    get_object_or_404,
    )

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny,
)

from district.models import District

from .models import Fair
from .pagination import DefaultNumberPagination
from .serializers import FairSerializer, FairUpdateSerializer


class FairCreateAPIView(CreateAPIView):
    """
    Fair CreateAPIView
    """

    queryset = Fair.objects.all()
    serializer_class = FairUpdateSerializer
    permission_classes = [AllowAny]


class FairListAPIView(ListAPIView):
    """
    Fair ListAPIView
    """

    pagination_class = DefaultNumberPagination
    permission_classes = [AllowAny]
    serializer_class = FairSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Fair.objects.all()

        filters = self.get_available_filter()
        if filters:
            queryset_list = queryset_list.filter(**filters)

        return queryset_list.order_by("id")

    def get_available_filter(self):
        selected_filters = {}
        available_filters = {
            "distrito": "district__name__icontains",
            "regiao5": "district__sub_prefecture__zone_8__zone_5__name__icontains",
            "nome_feira": "name__icontains",
            "bairro": "district__name__icontains",
        }
        for key, value in self.request.GET.items():
            if key in available_filters:
                selected_filters.update({available_filters[key]: value})
        return selected_filters


class FairRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Fair Retrieve, Update and DestroyAPIView
    """

    lookup_field = "id"
    permission_classes = [AllowAny]
    serializer_class = FairUpdateSerializer
    queryset = Fair.objects.all()
