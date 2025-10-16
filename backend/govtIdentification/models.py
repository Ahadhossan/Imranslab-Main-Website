from django.db import models

class NID(models.Model):
    name = models.CharField(max_length=255)
    nid_number = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Passport(models.Model):
    name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DriverLicense(models.Model):
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    vehicle_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name
