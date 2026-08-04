"""
==============================================================================
CONTACT FORMS
==============================================================================
"""

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Alex Mercer'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Inquiry subject'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Write your message...'}),
        }
