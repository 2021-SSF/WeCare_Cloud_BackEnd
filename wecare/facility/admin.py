from django.contrib import admin

# Register your models here.
from facility.models import Elders, Nurse, Diet

admin.site.register(Elders)
admin.site.register(Nurse)
admin.site.register(Diet)