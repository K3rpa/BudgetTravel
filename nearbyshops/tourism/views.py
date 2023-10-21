from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tourism
from .serializers import TourismSerializer

class TourismViews(APIView):
    def get(self,request):
        TourismModel = Tourism.objects.all()
        serializer = TourismSerializer(TourismModel, many=True)
        return Response({"TourismModel": serializer.data})
