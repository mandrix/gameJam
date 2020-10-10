from django.contrib import admin
from management.models import (
    Location,
    Province
)
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    model = Location

class ProvinceAdmin(admin.ModelAdmin):
    model = Province

admin.register(Province, ProvinceAdmin)

admin.register(Location, LocationAdmin)