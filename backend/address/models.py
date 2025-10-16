from django.db import models


class Address(models.Model):  # Address model is used to store the address information of the users.

    # Provinces in Bangladesh
    BANGLADESH_PROVINCES = [
        ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Khulna', 'Khulna'),
        ('Sylhet', 'Sylhet'),
        ('Barisal', 'Barisal'),
        ('Rangpur', 'Rangpur'),
        ('Rajshahi', 'Rajshahi'),
        ('Mymensingh', 'Mymensingh'),
    ]

    # Example cities and areas for dropdowns
    CITIES = [
        ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Khulna', 'Khulna'),
    ]

    AREAS = [
        ('Dhanmondi', 'Dhanmondi'),
        ('Gulshan', 'Gulshan'),
        ('Banani', 'Banani'),
        ('Motijheel', 'Motijheel'),
        ('Uttara', 'Uttara'),
    ]

    # max_length is a required argument that limits the maximum length of the field.
    # Why max_length=70?
    # UK Government Data Standards Catalogue suggests 35 characters for each of Given Name and Family Name, or 70 characters for a single field to hold the Full Name.
    id = models.AutoField(primary_key=True)  # Add this line
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100, default="Bangladesh")
    province = models.CharField(max_length=100, db_index=True, null=True) # Province is a state or a region.
    # db_index=True is used to create an index on the column in the database.
    city = models.CharField(max_length=100, db_index=True)
    area = models.CharField(max_length=100, db_index=True)
    road_street = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):  # __str__ method is used to return a human-readable representation of the object.
        return f"{self.name} - {self.city}, {self.area}"
