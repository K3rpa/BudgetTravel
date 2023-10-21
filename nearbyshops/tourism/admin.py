from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Tourism

@admin.register(Tourism)
class TourismAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address','state')