from django import forms
from .models import NID, Passport, DriverLicense

class NIDForm(forms.ModelForm):
    class Meta:
        model = NID
        fields = '__all__'

class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'

class LicenseForm(forms.ModelForm):
    class Meta:
        model = DriverLicense
        fields = '__all__'