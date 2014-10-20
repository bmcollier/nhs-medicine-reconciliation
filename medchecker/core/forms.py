from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'placeholder':'Username', 'autofocus': True}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class UnlockForm(forms.Form):
    pin = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'id': 'nfc-pin','placeholder':'PIN', 'autofocus': True, 'style': 'font-size: 2em; height: 2em;'}))