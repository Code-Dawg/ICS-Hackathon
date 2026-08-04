from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    """
    Form for player registration with username, email (optional), and password.
    """
    username = forms.CharField(
        max_length=150,
        help_text="Choose a unique player username.",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
