from address.models import Address
from django.test import TestCase, Client
from django.urls import reverse


class AddressViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            name="Jane Doe",
            phone_number="0423456789",
            country="Australia",
            province="VIC",
            city="Melbourne",
            area="Docklands",
            road_street="Collins Street",
            address="123 Collins Street, Docklands, Melbourne",
        )

    def test_address_list_view(self):
        response = self.client.get(reverse('address_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")

    def test_create_address_view(self):
        response = self.client.post(reverse('create_address'), {
            'name': "Alice Doe",
            'phone_number': "0434567890",
            'country': "Australia",
            'province': "QLD",
            'city': "Brisbane",
            'area': "South Bank",
            'road_street': "Grey Street",
            'address': "123 Grey Street, South Bank, Brisbane, QLD",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Address.objects.last().name, "Alice Doe")
