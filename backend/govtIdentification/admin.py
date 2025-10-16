from django.contrib import admin
from .models import NID, Passport, DriverLicense

admin.site.register(NID)
admin.site.register(Passport)
admin.site.register(DriverLicense)
