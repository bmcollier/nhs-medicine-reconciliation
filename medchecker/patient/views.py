from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from patient.models import Patient, PatientMedication, GPMedication, Medication
from patient.forms import PatientMedicationModelForm, BarcodeMedicationForm

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

    medications = Medication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED').order_by('status', 'virtual_medicinal_product__nm')
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
def scan_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    if request.method == 'POST':
        barcode_medication_form = BarcodeMedicationForm(request.POST)
        if barcode_medication_form.is_valid():
            barcode_medication = barcode_medication_form.save(commit=False)
            barcode_medication.patient = patient

            barcode_medication.save()

            return HttpResponseRedirect(
                reverse('patient_detail', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'

    else:
        barcode_medication_form = BarcodeMedicationForm() # An unbound form

    return render_to_response(
        'barcode_medication_form.html',
        context_instance=RequestContext(request, {'patient': patient, 'barcode_medication_form': barcode_medication_form})
        )

@login_required
def edit_medicine(request, patient_id, medicine_id=None):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    if request.method == 'POST':
        patient_medication_form = MedicationModelForm(request.POST)
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
        if medicine_id:
            med_ref = Medication.objects.get(id=medicine_id)
            patient_medication_form = PatientMedicationModelForm(instance=med_ref) # An unbound form
        else:
            patient_medication_form = PatientMedicationModelForm()
        
    return render_to_response(
        'edit_medicine_2.html',
        context_instance=RequestContext(request, {'patient': patient, 'patient_medication_form': patient_medication_form})
        )


@login_required
def reconcile_medicines(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    medications = Medication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED')
    categories = []
    
    for medication in medications:
        if medication.virtual_medicinal_product.vtmid.nm <> '':
            medication.category = medication.virtual_medicinal_product.vtmid.nm
            medication.display_name = medication.virtual_medicinal_product.nm
        else:
            medication.category = medication.virtual_therapeutic_moeity.nm
            medication.display_name = medication.virtual_medicinal_product.nm
        categories.append(medication.category)
        
    categories = set(categories)
    categories = list(categories)
    medications.order_by('category')
    
    return render_to_response(
        'reconcile_medicines.html',
        context_instance=RequestContext(request,
            {'patient': patient, 'medications': medications, 'categories': categories }
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