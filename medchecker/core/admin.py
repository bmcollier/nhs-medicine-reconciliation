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


class NfcUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = NfcUserCreationForm
    list_display = ("email", "nfc_login_id")
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'nhs_trust', 'role')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active')}
            ),
        )

    filter_horizontal = ()

admin.site.register(NfcUser, NfcUserAdmin)
