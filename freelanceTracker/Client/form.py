from django import forms
from .models import Client
class ClientForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = Client
        fields = ['first_name','last_name','email','platform','company']
