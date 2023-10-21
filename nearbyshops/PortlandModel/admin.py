from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Portland

@admin.register(Portland)
class PortlandAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address')