from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Chicago
from .serializers import ChicagoSerializer

class ChicagoModelViews(APIView):
    def get(self,request):
        ChicagoModel = Chicago.objects.all()
        serializer = ChicagoSerializer(ChicagoModel, many=True)
        return Response({"ChicagoModel": serializer.data})
