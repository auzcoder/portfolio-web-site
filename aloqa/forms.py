from django import forms
from aloqa.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'firstname',
            'lastname',
            'email',
            'message'
        ]

