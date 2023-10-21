from rest_framework_gis.serializers import GeoFeatureModelSerializer
from PortlandModel.models import Portland

class PortlandSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Portland
        geo_field = "location"
        fields = ('id','name','cost','address', 'city')