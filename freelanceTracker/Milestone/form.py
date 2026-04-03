from django import forms
from .models import Milestone

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['description','amount','due_date','is_paid']
        widgets = {
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'milestone description',
            }),
        }