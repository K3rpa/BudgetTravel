from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Austin
from .serializers import AustinSerializer

class AustinModelViews(APIView):
    def get(self,request):
        AustinModel = Austin.objects.all()
        serializer = AustinSerializer(AustinModel, many=True)
        return Response({"AustinModel": serializer.data})
