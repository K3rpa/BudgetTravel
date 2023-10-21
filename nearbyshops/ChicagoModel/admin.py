from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Chicago

@admin.register(Chicago)
class PortlandAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address')