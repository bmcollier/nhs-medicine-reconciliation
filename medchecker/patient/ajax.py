from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from patient.models import Patient, PatientMedication

import json

def verify_medicine(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    action = request.GET.get('action')
    med_type = request.GET.get('type')
    med_id = request.GET.get('medication_id')

    if med_type == 'patient':
        patient_medication = get_object_or_404(PatientMedication, id=med_id)
        if action == 'no':
            patient_medication.status = 'DELETED'
        if action == 'yes':
            patient_medication.status = 'TAKING'
        if action == 'not-as-prescribed':
            patient_medication.status = 'NOT AS PRESCRIBED'

        patient_medication.save()

    result = {'status': 'OK'}

    return HttpResponse(json.dumps(result), content_type='application/json')