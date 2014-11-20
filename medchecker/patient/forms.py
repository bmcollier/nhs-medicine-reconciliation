from django import forms
from django.forms.utils import ErrorDict

from patient.models import PatientMedication, Medication

from medicine.models import VirtualMedicinalProduct

class PatientMedicationModelForm(forms.ModelForm):
    medicine_free_text_shadow = forms.CharField(widget=forms.HiddenInput()) 

    class Meta:
        model = PatientMedication
        fields = ['patient',  'form', 'virtual_medicinal_product',
            'strength', 'route', 'dose', 'frequency', 'duration',
            'source', 'reason', 'comments', 'last_taken',
            ]
        widgets = {
            'virtual_medicinal_product': forms.TextInput(),
            'special_instructions': forms.Textarea(attrs={'rows': 3,}),
            'comments': forms.Textarea(attrs={'rows': 3,})
        }
        labels = {
            'virtual_medicinal_product': 'Medicine',
        }


    def clean(self):
        vmp_nm = self.data['virtual_medicinal_product']

        # Check to see if this text entered VMP exists in the database. If it
        # does, remove the validation errors.
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__exact=vmp_nm
                )

            if vmp is not None:
                del self.errors['virtual_medicinal_product']

                self.cleaned_data['virtual_medicinal_product'] = vmp

        except VirtualMedicinalProduct.DoesNotExist:
            pass # Just leave the field as it is (free-text).

        super(forms.ModelForm, self).clean()

    def clean_virtual_medicinal_product(self):
        print 'cleaning vmp'
        vmp_nm = self.cleaned_data['virtual_medicinal_product']
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__exact=vmp_nm
                )

            if vmp is not None:
                return vmp

        except VirtualMedicinalProduct.DoesNotExist:
            return vmp_nm


    def save(self, commit=True):
        # Save the provided password in hashed format
        patient_medication = super(forms.ModelForm, self).save(commit=False)

        if commit:
            patient_medication.save()
        return patient_medication

class BarcodeModelForm(forms.ModelForm):
    medicine_free_text_shadow = forms.CharField(widget=forms.HiddenInput()) 

    class Meta:
        model = Medication
        fields = ['patient',  'form', 'virtual_medicinal_product',
            'strength', 'route', 'dose', 'frequency', 'duration',
            'source', 'reason', 'comments', 'last_taken', 'dose_units',
            'daily_dose', 'daily_dose_units', 'quantity', 'virtual_therapeutic_moiety', 'classification_type'
            ]
        widgets = {
            'virtual_medicinal_product': forms.TextInput(),
            'special_instructions': forms.Textarea(attrs={'rows': 3,}),
            'comments': forms.Textarea(attrs={'rows': 3,})
        }
        labels = {
            'virtual_medicinal_product': 'Medicine',
        }


    def clean(self):
        vmp_nm = self.data['virtual_medicinal_product']

        # Check to see if this text entered VMP exists in the database. If it
        # does, remove the validation errors.
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__exact=vmp_nm
                )

            if vmp is not None:
                del self.errors['virtual_medicinal_product']

                self.cleaned_data['virtual_medicinal_product'] = vmp

        except VirtualMedicinalProduct.DoesNotExist:
            pass # Just leave the field as it is (free-text).

        super(forms.ModelForm, self).clean()

    def clean_virtual_medicinal_product(self):
        print 'cleaning vmp'
        vmp_nm = self.cleaned_data['virtual_medicinal_product']
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__exact=vmp_nm
                )

            if vmp is not None:
                return vmp

        except VirtualMedicinalProduct.DoesNotExist:
            return vmp_nm


    def save(self, commit=True):
        # Save the provided password in hashed format
        patient_medication = super(forms.ModelForm, self).save(commit=False)

        if commit:
            patient_medication.save()
        return patient_medication


class MedicationModelForm(forms.ModelForm):
    medicine_free_text_shadow = forms.CharField(widget=forms.HiddenInput()) 

    class Meta:
        model = Medication
        fields = ['patient',  'form', 'virtual_medicinal_product',
            'strength', 'route', 'dose', 'frequency', 'duration',
            'source', 'reason', 'comments', 'last_taken', 'dose_units',
            'daily_dose', 'daily_dose_units', 'quantity', 'virtual_therapeutic_moiety', 'classification_type'
            ]
        widgets = {
            'virtual_medicinal_product': forms.TextInput(),
            'special_instructions': forms.Textarea(attrs={'rows': 3,}),
            'comments': forms.Textarea(attrs={'rows': 3,})
        }
        labels = {
            'virtual_medicinal_product': 'Medicine',
        }


    def clean(self):
        vmp_nm = self.data['virtual_medicinal_product']

        # Check to see if this text entered VMP exists in the database. If it
        # does, remove the validation errors.
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__exact=vmp_nm
                )

            if vmp is not None:
                del self.errors['virtual_medicinal_product']

                self.cleaned_data['virtual_medicinal_product'] = vmp

        except VirtualMedicinalProduct.DoesNotExist:
            pass # Just leave the field as it is (free-text).

        super(forms.ModelForm, self).clean()

    def clean_virtual_medicinal_product(self):
        print 'cleaning vmp'
        vmp_nm = self.cleaned_data['virtual_medicinal_product']
        try:
            vmp = VirtualMedicinalProduct.objects.get(
                nm__exact=vmp_nm
                )

            if vmp is not None:
                return vmp

        except VirtualMedicinalProduct.DoesNotExist:
            return vmp_nm


    def save(self, commit=True):
        # Save the provided password in hashed format
        patient_medication = super(forms.ModelForm, self).save(commit=False)

        if commit:
            patient_medication.save()
        return patient_medication

class EditMedicationModelForm(forms.ModelForm):
    medicine_free_text_shadow = forms.CharField(widget=forms.HiddenInput()) 

    class Meta:
        model = Medication
        fields = ['patient',  'form',
            'strength', 'route', 'dose', 'frequency', 'duration',
            'source', 'reason', 'comments', 'last_taken', 'dose_units',
            'daily_dose', 'daily_dose_units', 'quantity', 'virtual_therapeutic_moiety'
            ]
        widgets = {
            #'virtual_medicinal_product': forms.TextInput(),
            'special_instructions': forms.Textarea(attrs={'rows': 3,}),
            'comments': forms.Textarea(attrs={'rows': 3,})
        }



    def clean(self):
       super(forms.ModelForm, self).clean()

    def save(self, commit=True):
        # Save the provided password in hashed format
        patient_medication = super(forms.ModelForm, self).save(commit=False)

        if commit:
            patient_medication.save()
        return patient_medication

