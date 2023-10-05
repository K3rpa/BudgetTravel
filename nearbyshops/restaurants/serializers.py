from rest_framework_gis.serializers import GeoFeatureModelSerializer
from restaurants.models import Restaurant

class RestaurantSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Restaurant
        geo_field = "location"
        fields = ('name','address', 'city')
        # bbox_geo_field = 'bbox_geometry'