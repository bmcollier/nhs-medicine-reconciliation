from django.contrib import admin

from patient.models import Patient, PatientMedication, GPMedication

class PatientAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientMedication)
admin.site.register(GPMedication)