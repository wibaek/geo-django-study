from django.urls import path

from .views import WorldBorderView, WorldBorderNearbyView

urlpatterns = [
    path("", WorldBorderView.as_view(), name="index"),
    path("nearby/", WorldBorderNearbyView.as_view(), name="nearby"),
]
