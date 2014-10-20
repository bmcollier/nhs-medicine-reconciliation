from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from patient.models import Patient, PatientMedication
from patient.forms import PatientMedicationModelForm

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

    unverified_medications = PatientMedication.objects.filter(patient=patient)

    return render_to_response(
        'detail.html',
        context_instance=RequestContext(request,
            {'patient': patient,
            'unverified_medications': unverified_medications}
            )
        )

@login_required
def add_medicine(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient_medication_form = PatientMedicationModelForm(request.POST)
        if patient_medication_form.is_valid():
            patient_medication = patient_medication_form.save(commit=False)
            patient_medication.patient = patient

            patient_medication.save()

            return HttpResponseRedirect(
                reverse('patient_detail', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'

    else:
        patient_medication_form = PatientMedicationModelForm() # An unbound form

    return render_to_response(
        'add_medicine.html',
        context_instance=RequestContext(request, {'patient': patient, 'patient_medication_form': patient_medication_form})
        )

@login_required
def reconcile_medicine(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    unverified_medications = PatientMedication.objects.filter(patient=patient)

    return render_to_response(
        'reconcile_medicine.html',
        context_instance=RequestContext(request,
            {'patient': patient,
            'unverified_medications': unverified_medications}
            )
        )