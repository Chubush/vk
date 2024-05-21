from django import forms
from account.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["isim", "email", "konu", "mesaj"]