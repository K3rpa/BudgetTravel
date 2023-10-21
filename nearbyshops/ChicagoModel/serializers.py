from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ChicagoModel.models import Chicago

class ChicagoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Chicago
        geo_field = "location"
        fields = ('id','name','cost','address', 'city')