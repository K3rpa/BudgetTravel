from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Manhattan

@admin.register(Manhattan)
class ManhattanAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address')