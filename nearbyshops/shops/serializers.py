from rest_framework_gis.serializers import GeoFeatureModelSerializer
from shops.models import Shop

class ShopSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Shop
        geo_field = "location"
        fields = ('id','name','cost','address', 'city')
        # bbox_geo_field = 'bbox_geometry'