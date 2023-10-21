from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Manhattan
from .serializers import ManhattanSerializer

class ManhattanModelViews(APIView):
    def get(self,request):
        ManhattanModel = Manhattan.objects.all()
        serializer = ManhattanSerializer(ManhattanModel, many=True)
        return Response({"ManhattanModel": serializer.data})
