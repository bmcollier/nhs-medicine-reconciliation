from django.contrib import admin

from patient.models import Patient

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

admin.site.register(Patient, PatientAdmin)