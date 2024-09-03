from django.urls import path

from .views import WorldBorderView, WorldBorderNearbyView, WorldBorderFilteredView

urlpatterns = [
    path("", WorldBorderView.as_view(), name="index"),
    path("nearby/", WorldBorderNearbyView.as_view(), name="nearby"),
    path("distance/", WorldBorderFilteredView.as_view(), name="distance"),
]
