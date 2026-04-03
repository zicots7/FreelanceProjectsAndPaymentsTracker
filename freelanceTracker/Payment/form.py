from django import forms
from .models import Payment

class paymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'milestone','amount_paid','date_paid','payment_method']
        widgets = {
            'date_paid': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            })
        }