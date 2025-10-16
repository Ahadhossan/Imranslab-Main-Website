from django.shortcuts import render, get_object_or_404, redirect
from .models import NID, Passport, DriverLicense
from .forms import NIDForm, PassportForm, LicenseForm

# Landing page
def govt_identification_home(request):
    return render(request, 'govtIdentification/home.html')

# CRUD views for NID
def nid_list(request):
    nids = NID.objects.all()
    return render(request, 'govtIdentification/nid_list.html', {'nids': nids})

def nid_add(request):
    if request.method == 'POST':
        form = NIDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nid_list')
    else:
        form = NIDForm()
    return render(request, 'govtIdentification/nid_form.html', {'form': form})

def nid_edit(request, pk):
    nid = get_object_or_404(NID, pk=pk)
    if request.method == 'POST':
        form = NIDForm(request.POST, instance=nid)
        if form.is_valid():
            form.save()
            return redirect('nid_list')
    else:
        form = NIDForm(instance=nid)
    return render(request, 'govtIdentification/nid_form.html', {'form': form})

def nid_delete(request, pk):
    nid = get_object_or_404(NID, pk=pk)
    if request.method == 'POST':
        nid.delete()
        return redirect('nid_list')
    return render(request, 'govtIdentification/nid_confirm_delete.html', {'nid': nid})

# CRUD views for Passport
def passport_list(request):
    passports = Passport.objects.all()
    return render(request, 'govtIdentification/passport_list.html', {'passports': passports})

def passport_add(request):
    if request.method == 'POST':
        form = PassportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passport_list')
    else:
        form = PassportForm()
    return render(request, 'govtIdentification/passport_form.html', {'form': form})

def passport_edit(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    if request.method == 'POST':
        form = PassportForm(request.POST, instance=passport)
        if form.is_valid():
            form.save()
            return redirect('passport_list')
    else:
        form = PassportForm(instance=passport)
    return render(request, 'govtIdentification/passport_form.html', {'form': form})

def passport_delete(request, pk):
    passport = get_object_or_404(Passport, pk=pk)
    if request.method == 'POST':
        passport.delete()
        return redirect('passport_list')
    return render(request, 'govtIdentification/passport_confirm_delete.html', {'passport': passport})

# CRUD views for DriverLicense
def license_list(request):
    licenses = DriverLicense.objects.all()
    return render(request, 'govtIdentification/license_list.html', {'licenses': licenses})

def license_add(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('license_list')
    else:
        form = LicenseForm()
    return render(request, 'govtIdentification/license_form.html', {'form': form})

def license_edit(request, pk):
    license = get_object_or_404(DriverLicense, pk=pk)
    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            return redirect('license_list')
    else:
        form = LicenseForm(instance=license)
    return render(request, 'govtIdentification/license_form.html', {'form': form})

def license_delete(request, pk):
    license = get_object_or_404(DriverLicense, pk=pk)
    if request.method == 'POST':
        license.delete()
        return redirect('license_list')
    return render(request, 'govtIdentification/license_confirm_delete.html', {'license': license})
