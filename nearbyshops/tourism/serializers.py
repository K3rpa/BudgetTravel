from rest_framework_gis.serializers import GeoFeatureModelSerializer
from tourism.models import Tourism

class TourismSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Tourism
        geo_field = "location"
        fields = ('id','name','cost','address', 'city','state')