from address.models import Address
from django.test import TestCase


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            name="John Doe",
            phone_number="0412345678",
            country="Australia",
            province="NSW",
            city="Sydney",
            area="Central Business District",
            road_street="George Street",
            address="123 George Street, Central Business District, Sydney, NSW",
        )

    def test_model_creation(self):
        self.assertEqual(self.address.city, "Sydney")
        self.assertEqual(self.address.name, "John Doe")

    def test_str_representation(self):
        self.assertEqual(str(self.address), "John Doe - Sydney, Central Business District")
