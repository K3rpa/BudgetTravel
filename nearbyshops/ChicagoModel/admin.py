from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Chicago

@admin.register(Chicago)
class RestaurantAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address')