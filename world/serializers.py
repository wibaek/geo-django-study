from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import WorldBorder


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"
        fields = "__all__"
        auto_bbox = True
