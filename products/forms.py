from django import forms
from .models import ContactSubmission

class CcontactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name','email']
