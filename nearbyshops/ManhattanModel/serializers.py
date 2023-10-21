from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ManhattanModel.models import Manhattan

class ManhattanSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Manhattan
        geo_field = "location"
        fields = ('id','name','cost','address', 'city')