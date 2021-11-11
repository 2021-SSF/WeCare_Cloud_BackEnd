from django.contrib import admin

# Register your models here.
from hospital_admin.models import Hospital, Adminster, Room, Bed

admin.site.register(Hospital)
admin.site.register(Adminster)
admin.site.register(Room)
admin.site.register(Bed)