from django.http import HttpResponse

from medicine.medicineparser import get_medicine_text_as_components

import json

def parse_medicine_text(request):
    medicine_string = request.GET.get('medicine_free_text')

    medicine_dict_json = json.dumps(get_medicine_text_as_components(medicine_string))

    return HttpResponse(medicine_dict_json, content_type='application/json')