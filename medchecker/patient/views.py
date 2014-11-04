from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from patient.models import Patient, PatientMedication, GPMedication
from patient.forms import PatientMedicationModelForm

@login_required
def search(request):
    patients = Patient.objects.all().order_by('first_name', 'last_name')

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
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    medications = PatientMedication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED').order_by('status', 'virtual_medicinal_product__nm')
    # verified_medications = PatientMedication.objects.select_related('virtual_medicinal_product').filter(patient=patient, status='VERIFIED')

    return render_to_response(
        'detail.html',
        context_instance=RequestContext(request,
            {'patient': patient, 'medications': medications,}
            )
        )

@login_required
def add_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

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
def edit_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

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
        'edit_medicine.html',
        context_instance=RequestContext(request, {'patient': patient, 'patient_medication_form': patient_medication_form})
        )


@login_required
def reconcile_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    history_medications = PatientMedication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED')
    gp_medications = GPMedication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED')

    medications_dict = {}
    for medication in history_medications:
        if medications_dict.get(str(medication.virtual_medicinal_product.vtmid.vtmid)):
            current_dict = medications_dict[str(medication.virtual_medicinal_product.vtmid.vtmid)]
            new_dict = dict(current_dict.items() + {'history': medication,}.items())
            medications_dict[str(medication.virtual_medicinal_product.vtmid.vtmid)] = new_dict
        else:
            medications_dict[str(medication.virtual_medicinal_product.vtmid.vtmid)] = {
                'history': medication,
                'medinfo': {
                    'vpid': medication.virtual_medicinal_product.vpid, 'nm': medication.virtual_medicinal_product.nm
                    }
                }

    for medication in gp_medications:
        if medications_dict.get(str(medication.virtual_medicinal_product.vtmid.vtmid)):
            current_dict = medications_dict[str(medication.virtual_medicinal_product.vtmid.vtmid)]
            new_dict = dict(current_dict.items() + {'gp': medication,}.items())
            medications_dict[str(medication.virtual_medicinal_product.vtmid.vtmid)] = new_dict
        else:
            medications_dict[str(medication.virtual_medicinal_product.vtmid.vtmid)] = {
                'gp': medication,
                'medinfo': {
                    'vpid': medication.virtual_medicinal_product.vpid, 'nm': medication.virtual_medicinal_product.nm
                    }
                }

    medications = []
    for k, v in medications_dict.iteritems():
        medications += [v,]

    return render_to_response(
        'reconcile_medicine.html',
        context_instance=RequestContext(request,
            {'patient': patient, 'medications': medications}
            )
        )

@login_required
def verify_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)
    
    medications = PatientMedication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED').order_by('status')

    return render_to_response(
        'verify_medicine.html',
        context_instance=RequestContext(request, 
            {'patient': patient, 'medications': medications}
            )
        )

@login_required
def discharge(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)
    return render_to_response(
        'discharge.html',
        context_instance=RequestContext(request, {'patient': patient,})
        )