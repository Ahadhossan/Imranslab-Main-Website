from django import forms

from .models import Address


# why below line important?
# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#modelform
class AddressForm(
    forms.ModelForm):  # This form is used to create a form for the Address model. The form is created using the ModelForm class provided by Django.
    class Meta:  # The Meta class is used to define the model and fields that will be used to create the form.
        model = Address
        fields = '__all__'

        # https://docs.djangoproject.com/en/3.2/ref/forms/fields/#choices
