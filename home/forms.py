from django import forms
from .models import Feedback

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

