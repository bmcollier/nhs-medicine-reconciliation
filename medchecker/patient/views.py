from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
 
from patient.models import Patient, PatientMedication, GPMedication, Medication
from patient.forms import MedicationModelForm, BarcodeModelForm, EditMedicationModelForm

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
        patient_medication_form = MedicationModelForm(request.POST)
        if patient_medication_form.is_valid():
            patient_medication = patient_medication_form.save(commit=False)
            patient_medication.patient = patient
            patient_medication.classification_type='OTHER';
            patient_medication.save()

            return HttpResponseRedirect(
                reverse('patient_reconcile_medicine', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'

    else:
        patient_medication_form = MedicationModelForm() # An unbound form
    return render_to_response(
        'add_medicine.html',
        context_instance=RequestContext(request, {'patient': patient, 'patient_medication_form': patient_medication_form})
        )

def add_medicine_last(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    if request.method == 'POST':
        patient_medication_form = MedicationModelForm(request.POST)
        if patient_medication_form.is_valid():
            patient_medication = patient_medication_form.save(commit=False)
            patient_medication.patient = patient
            patient_medication.classification_type='EHR';
            patient_medication.save()

            return HttpResponseRedirect(
                reverse('patient_reconcile_medicine', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'

    else:
        patient_medication_form = MedicationModelForm() # An unbound form
    return render_to_response(
        'add_medicine_last.html',
        context_instance=RequestContext(request, {'patient': patient, 'patient_medication_form': patient_medication_form})
        )
    
def add_medicine_gp(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    if request.method == 'POST':
        patient_medication_form = MedicationModelForm(request.POST)
        if patient_medication_form.is_valid():
            patient_medication = patient_medication_form.save(commit=False)
            patient_medication.patient = patient
            patient_medication.classification_type='GP';
            patient_medication.save()

            return HttpResponseRedirect(
                reverse('patient_reconcile_medicine', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'

    else:
        patient_medication_form = MedicationModelForm() # An unbound form
    return render_to_response(
        'add_medicine_gp.html',
        context_instance=RequestContext(request, {'patient': patient, 'patient_medication_form': patient_medication_form})
        )


@login_required
def edit_medicine(request, patient_id, medication_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)

    if request.method == 'POST':
        a = Medication.objects.get(id=medication_id)
        patient_medication_form = EditMedicationModelForm(request.POST, instance=a)
        if patient_medication_form.is_valid():
            patient_medication = patient_medication_form.save(commit=False)
            patient_medication.patient = patient

            patient_medication.save()

            return HttpResponseRedirect(
                reverse('patient_reconcile_medicine', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'

    else:
        a = Medication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').get(id=medication_id)
        patient_medication_form = EditMedicationModelForm(instance=a)
    return render_to_response(
        'edit_medicine.html',
        context_instance=RequestContext(request, {'patient': patient, 'medication': a, 'patient_medication_form': patient_medication_form})
        )

@login_required
def scan_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)
    if request.method == 'POST':
        patient_medication_form = BarcodeModelForm(request.POST)
        if patient_medication_form.is_valid():
            patient_medication = patient_medication_form.save(commit=False)
            patient_medication.patient = patient
            patient_medication.classification_type='OTHER'
            patient_medication.save()

            return HttpResponseRedirect(
                reverse('patient_reconcile_medicine', kwargs={'patient_id': patient.id,})
                )
        else:
            print 'not valid'
    else:
        patient_medication_form = BarcodeModelForm() # An unbound form

    return render_to_response(
        'scan_medicine.html',
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
            medication.display_name = medication.virtual_medicinal_product.vtmid.nm
        else:
            medication.category = medication.virtual_medicinal_product.vtmid.nm
            medication.display_name = medication.virtual_medicinal_product.nm
        categories.append(medication.category)
        
    categories = set(categories)
    categories = list(categories)
    medications.order_by('category')
    
    return render_to_response(
        'reconcile_medicines.html',
        context_instance=RequestContext(request,
            {'patient': patient, 'medications': medications, 'categories': categories, 'patient_edit_link': '/patient/' + patient_id + '/add_medication/', 'patient_edit_link_gp': '/patient/' + patient_id + '/add_medication_gp/', 'patient_edit_link_ehr': '/patient/' + patient_id + '/add_medication_last/' }
            )
        )

@login_required
def reconcile_discharge(request, patient_id):
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
        'reconcile_discharge.html',
        context_instance=RequestContext(request,
            {'patient': patient, 'medications': medications, 'categories': categories }
            )
        )


@login_required
def verify_medicine(request, patient_id):
    patient = get_object_or_404(Patient.objects.select_related('general_practitioner'), id=patient_id)
    
    medications = Medication.objects.select_related('virtual_medicinal_product', 'virtual_medicinal_product__vtmid').filter(patient=patient).exclude(status='2 DELETED').order_by('status')

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