from django import forms
from .models import Guest, contectUs, Enquiry


class guestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ("name", "email", "description")


class contactForm(forms.ModelForm):
    class Meta:
        model = contectUs
        fields = ("name", "email", "number", "comment")


class enquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"
