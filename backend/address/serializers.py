from rest_framework import serializers

from .models import Address


# This file is used to serialize the Address model. Serializing the model allows us to convert the model data into JSON format so that it can be easily rendered into a template or used in an API.
# The Address model is imported from the models.py file. The Address model is used to create the fields that will be serialized.

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
