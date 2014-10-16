from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from patient.models import Patient

@login_required
def search(request):
    patients = Patient.objects.all()

    return render_to_response(
        'search.html',
        context_instance=RequestContext(request, {'patients': patients})
        )

@login_required
def add(request):
    return render_to_response(
        'add.html',
        context_instance=RequestContext(request,)
        )

@login_required
def detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    return render_to_response(
        'detail.html',
        context_instance=RequestContext(request, {'patient': patient})
        )