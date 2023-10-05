from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Shop
from .serializers import ShopSerializer

class ShopViews(APIView):
    def get(self,request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response({"shops": serializer.data})
