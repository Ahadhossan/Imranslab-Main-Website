
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import AddressForm
from .models import Address
from .serializers import AddressSerializer


# Create
def create_address(
        request):  # This view function is used to create a new address. The view function renders a form to create a new address. The form is created using the AddressForm class defined in the forms.py file.
    if request.method == 'POST':  # The view function checks if the request method is POST. If the request method is POST, the view function saves the form data to the database and redirects the user to the address list view.
        form = AddressForm(
            request.POST)  # The view function creates a new instance of the AddressForm class with the form data.
        # how to know form is valid or not?
        # https://www.django-rest-framework.org/api-guide/requests/#form-data
        if form.is_valid():  # The view function checks if the form is valid. If the form is valid, the view function saves the form data to the database and redirects the user to the address list view.
            form.save()  # The view function saves the form data to the database.
            # 'address_list' is the name of the URL pattern
            # where you see that pattern defined in urls.py
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'address/create_address.html', {'form': form})

# Read (List)
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address/address_list.html', {'addresses': addresses})

# Update
def update_address(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if not form.is_valid():
            print(form.errors)  # Debugging form validation errors
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'address/update_address.html', {'form': form})

# Delete
def delete_address(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'address/delete_address.html', {'address': address})


class AddressViewSet(
    viewsets.ModelViewSet):  # This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'

@api_view(['POST'])
def bulk_create_addresses(request):
    serializer = AddressSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)