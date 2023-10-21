from rest_framework_gis.serializers import GeoFeatureModelSerializer
from AustinModel.models import Austin

class AustinSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Austin
        geo_field = "location"
        fields = ('id','name','cost','address', 'city')