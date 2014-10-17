from django import forms

from patient.models import PatientMedication

from medicine.models import VirtualMedicinalProductPack

# class PatientForm(forms.ModelForm):
#     def clean_nhs_number(self):
        
#         entered_nhs_number = self.cleaned_data["nhs_number"]

#         return self.cleaned_data["name"]

class PatientMedicationModelForm(forms.ModelForm):



    class Meta:
        model = PatientMedication
        fields = ['patient',  'form', 'virtual_medicinal_product_pack',
            'strength', 'dose', 'frequency', 'duration',
            'special_instructions', 'source', 'reason', 'comments',
            ]
        widgets = {
            'virtual_medicinal_product_pack': forms.TextInput()
        }
        labels = {
            'virtual_medicinal_product_pack': 'Medicine',
        }

    def clean_virtual_medicinal_product_pack(self):
        print 'cleaning vmpp'
        vmpp_nm = self.cleaned_data["virtual_medicinal_product_pack"]

        vmpp = VirtualMedicinalProductPack.objects.get(nm=vmpp_nm)

        print vmpp

        print vmpp.id

        return vmpp.vppid_id