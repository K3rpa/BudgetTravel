from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.gis.measure import D
from django.contrib.gis.db.models import PointField

from .models import Tourism
from .serializers import TourismSerializer

class TourismViews(APIView):
    def get(self,request):
        TourismModel = Tourism.objects.all()
        serializer = TourismSerializer(TourismModel, many=True)
        return Response({"TourismModel": serializer.data})

    def post(self,request,format=None):
        search_query = (request.data).split(",")
        lat = int(search_query[0])
        long = int(search_query[1])
        base_point = PointField(lat,long)
        tourism = Tourism.objects
        #nearby queries within 150 km
        matched_data = tourism.filter(
            location__distance_lte=(
                base_point, D(km=150))
                ).distance(base_point).order_by('distance')
        serializer = TourismSerializer(matched_data,many=True)    
        return Response(data=serializer.data)
