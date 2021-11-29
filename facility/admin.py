from django.contrib import admin

# Register your models here.
from facility.models import Room, Bed, Elder, ElderStatus, Violence, OccupancyGraph

admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(Elder)
admin.site.register(ElderStatus)
admin.site.register(Violence)
admin.site.register(OccupancyGraph)