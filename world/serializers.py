from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import WorldBorder


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"
        fields = "__all__"
        # auto_bbox = True
        bbox_geo_field = "mpoly"  # auto_bbox나 bbox_get_field 둘 중 하나만 사용해야 함
