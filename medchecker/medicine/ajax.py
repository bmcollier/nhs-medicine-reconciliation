from django.http import HttpResponse
from django.utils.html import strip_tags

from medicine.medicineparser import (get_medicine_text_as_components,
    INTERVAL_FREQUENCY_HUMAN_MAP, DAILY_REPETITION_HUMAN_MAP, FORM_HUMAN_MAP, 
    ROUTE_HUMAN_MAP, clean_token)
from medicine.models import VirtualMedicinalProduct, ActualMedicinalProduct, ActualMedicinalProductPack
from patient.models import Medication, Patient

import json

def delete_medicine(request):
    medicine = Medication(id=request.GET.get('medication_id'))
    medicine.delete();
    return HttpResponse("", content_type='application/json')

def drop_medicine(request):
    patient_name = Patient(id=request.GET.get('patient_id'))
    vmp_name = VirtualMedicinalProduct(vpid=request.GET.get('vmp'))
    new_medicine = Medication(patient=patient_name,
                              dose=request.GET.get('dose'),
                              daily_dose_units = request.GET.get('daily_dose_units'),
                              route = request.GET.get('route'),
                              frequency = request.GET.get('frequency'),
                              virtual_medicinal_product=vmp_name, 
                              source=request.GET.get('source'),
                              strength=request.GET.get('strength'),
                              classification_type=request.GET.get('classification'))
    # Now return new medicine id
    
    new_medicine.save()
    return HttpResponse('{"id":"' + str(new_medicine.id) + '"}', content_type='application/json')
    
def suggest_barcode(request):
    medicine_barcode = request.GET.get('medicine_barcode')
    medicine = ActualMedicinalProductPack.objects.get(gtin=medicine_barcode)
    medicine_name_suggestion = '{"name": "' + medicine.vppid.vpid.nm + '","authority":"' + medicine.nm + '"}'
    return HttpResponse(medicine_name_suggestion, content_type='application/json')

def parse_medicine_text(request):
    medicine_string = request.GET.get('medicine_free_text')
    medicine_string = strip_tags(medicine_string.lower())
    current_term = clean_token(medicine_string[medicine_string.rfind(',') + 1:])

    parsed_meds = get_medicine_text_as_components(medicine_string)

    parsed_meds['suggestions'] = []
    suggestions = []
    if parsed_meds.get('medicine_is_valid', False):
        print 'doing new suggestions'

        if not parsed_meds.get('form', False):
            suggestions += set([v for k, v in FORM_HUMAN_MAP.items()])

        if not parsed_meds.get('frequency', False):
            suggestions += set([v for k, v in INTERVAL_FREQUENCY_HUMAN_MAP.items()])

        # if not parsed_meds.get('duration', False):
        #     suggestions += set([v for k, v in DAILY_REPETITION_HUMAN_MAP.items()])

        if not parsed_meds.get('route', False):
            suggestions += set([v for k, v in ROUTE_HUMAN_MAP.items()])

        for s in suggestions:
            if s.startswith(current_term):
                parsed_meds['suggestions'] += [s]

        parsed_meds['suggestions'] = sorted(parsed_meds['suggestions'], key=str.lower)

    else:
        medicine = parsed_meds.get('medicine')
        if medicine:
            suggested_meds = VirtualMedicinalProduct.objects.filter(nm__istartswith=medicine).distinct('nm').order_by('nm')

            meds = []
            for med in suggested_meds:
                meds += [med.nm]

            parsed_meds['suggestions'] = meds

    medicine_dict_json = json.dumps(parsed_meds)

    return HttpResponse(medicine_dict_json, content_type='application/json')