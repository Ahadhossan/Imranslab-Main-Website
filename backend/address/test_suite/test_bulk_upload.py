import csv, os
from address.models import Address
import tempfile
from django.test import TestCase

class BulkUploadTest(TestCase):
    def setUp(self):
        # Create a sample CSV file
        temp_dir = tempfile.gettempdir()
        self.csv_file_path = f"{temp_dir}/test_addresses.csv"
        with open(self.csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "name",
                "phone_number",
                "country",
                "province",
                "city",
                "area",
                "road_street",
                "address"
            ])
            for i in range(1, 101):  # Add 100 records
                writer.writerow([
                    f"Name{i}",
                    f"12345678{i:02d}",
                    f"Country{i}",
                    f"Province{i}",
                    f"City{i}",
                    f"Area{i}",
                    f"Street{i}",
                    f"Address{i}"
                ])

    def test_bulk_upload(self):
        with open(self.csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Address.objects.create(
                    name=row["name"],
                    phone_number=row["phone_number"],
                    country=row["country"],
                    province=row["province"],
                    city=row["city"],
                    area=row["area"],
                    road_street=row["road_street"],
                    address=row["address"]  # Add the "address" field
                )

        # Check if all 100 records were created
        self.assertEqual(Address.objects.count(), 100)
        first_address = Address.objects.first()
        self.assertEqual(first_address.city, "City1")
        self.assertEqual(first_address.name, "Name1")
