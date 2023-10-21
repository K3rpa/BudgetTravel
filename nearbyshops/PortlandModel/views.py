from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Portland
from .serializers import PortlandSerializer

class PortlandModelViews(APIView):
    def get(self,request):
        PortlandModel = Portland.objects.all()
        serializer = PortlandSerializer(PortlandModel, many=True)
        return Response({"PortlandModel": serializer.data})
