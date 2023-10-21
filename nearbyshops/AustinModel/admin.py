from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Austin

@admin.register(Austin)
class AustinAdmin(OSMGeoAdmin):
    list_display = ('name', 'location','address')