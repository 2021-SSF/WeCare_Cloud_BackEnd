from django.contrib import admin

# Register your models here.
from hospital.models import Patient, Nurse, Diet

admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Diet)
