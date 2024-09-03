from django.db.models import F
from rest_framework import generics

from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import Func, GeometryField
from django.contrib.gis.db.models.functions import Distance

from .models import WorldBorder
from .serializers import WorldBorderSerializer


class GeojsonLocationList(generics.ListCreateAPIView):
    # -- other omitted view attributes --- #
    pagination_class = GeoJsonPagination
    pagination_class.page_size = 1


class WorldBorderView(generics.ListAPIView):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    pagination_class = GeoJsonPagination
    # bbox_filter_field = "mpoly"
    # bbox_filter_include_overlapping = True
    # filter_backends = (InBBoxFilter,)


class WorldBorderNearbyView(generics.ListAPIView):
    serializer_class = WorldBorderSerializer

    def get_queryset(self):
        lat, lng = self.request.query_params.get("lat"), self.request.query_params.get(
            "lng"
        )
        if lat is None or lng is None:
            raise ValueError("lat와 lng를 입력해주세요.")

        point = Point(float(lng), float(lat), srid=4326)

        # Method 1: mpoly 필드를 이용
        return WorldBorder.objects.annotate(distance=Distance("mpoly", point)).order_by(
            "distance"
        )[:1]

        # Method 2: lat, lon 필드를 이용
        return WorldBorder.objects.annotate(
            distance=Distance(
                Func(
                    F("lon"),
                    F("lat"),
                    function="ST_MakePoint",
                    output_field=GeometryField(),
                ),
                point,
            )
        ).order_by("distance")[:1]
