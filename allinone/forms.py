from django import forms


class UserForm(forms.Form):
    full_name = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField(required=False, empty_value=None)
