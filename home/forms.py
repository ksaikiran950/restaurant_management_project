from django import forms
from .models import Feedback,ContactSubmission

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback        
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Enter your feedback here...'
                })
}



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission        
        fields = ['name', 'email']