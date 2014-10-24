from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from core.models import NfcUser

class NfcUserCreationForm(forms.ModelForm):
    class Meta:
        model = NfcUser
        fields = '__all__'

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(forms.ModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        
        if not self.data['username']:
            self.cleaned_data['username'] = self.data['email'][:30]
        
        try:
            del self.errors['username']
        except KeyError:
            pass

        self.cleaned_data['password'] = 'fivium12'


        try:
            del self.errors['password']
        except KeyError:
            pass

        super(forms.ModelForm, self).clean()


class NfcUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = NfcUserCreationForm
    list_display = ("first_name", "last_name", "email", "nfc_url")
    ordering = ("first_name", "last_name", "email",)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'nhs_trust', 'role')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'nhs_trust', 'role')}
            ),
        )

    filter_horizontal = ()

admin.site.register(NfcUser, NfcUserAdmin)
