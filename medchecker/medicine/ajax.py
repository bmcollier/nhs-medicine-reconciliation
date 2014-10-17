from django.http import HttpResponse

from medicine.medicineparser import get_medicine_text_as_components
from medicine.models import ActualMedicinalProduct

import json

def parse_medicine_text(request):
    medicine_string = request.GET.get('medicine_free_text')

    parsed_meds = get_medicine_text_as_components(medicine_string)

    try:
        medicine = parsed_meds['medicine']

        print medicine

        suggested_meds = ActualMedicinalProduct.objects.filter(nm__icontains=medicine).distinct('nm')

        print suggested_meds

        meds = []
        for med in suggested_meds:
            meds += [med.nm]

        parsed_meds['suggestions'] = meds

    except KeyError:
        pass

    medicine_dict_json = json.dumps(parsed_meds)

    return HttpResponse(medicine_dict_json, content_type='application/json')