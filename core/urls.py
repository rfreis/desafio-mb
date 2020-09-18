from django.urls import path

from .views import (
    FairCreateAPIView,
    FairListAPIView,
    FairRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path("fair/", FairListAPIView.as_view(), name="list-fair"),
    path("fair/create/", FairCreateAPIView.as_view(), name="create-fair"),
    path(
        "fair/<int:id>/",
        FairRetrieveUpdateDestroyAPIView.as_view(),
        name="detail-fair",
    ),
]
