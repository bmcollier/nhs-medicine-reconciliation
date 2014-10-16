class PatientForm(forms.ModelForm):
    def clean_nhs_number(self):
        
        entered_nhs_number = self.cleaned_data["nhs_number"]

        return self.cleaned_data["name"]