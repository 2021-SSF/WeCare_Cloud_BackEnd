from django.contrib import admin

# Register your models here.
from facility_admin.models import Facility, Adminster, Room, Bed

admin.site.register(Facility)
admin.site.register(Adminster)
admin.site.register(Room)
admin.site.register(Bed)