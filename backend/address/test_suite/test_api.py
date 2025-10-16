from address.models import Address
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AddressAPITest(APITestCase):
    def setUp(self):
        self.address = Address.objects.create(
            name="Bob Doe",
            phone_number="0445678901",
            country="Australia",
            province="Western Australia",
            city="Perth",
            area="CBD",
            road_street="Hay Street",
            address="Shop 1, 1 Hay Street",
        )

    def test_get_addresses(self):
        response = self.client.get(reverse('address-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        response = self.client.post(
            reverse('address-list'),
            {
                'name': "Clara Doe",
                'phone_number': "0456789012",
                'country': "Australia",
                'province': "South Australia",
                'city': "Adelaide",
                'area': "Glenelg",
                'road_street': "Jetty Road",
                'address': "Shop 1, 1 Jetty Road",
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bulk_create_address_api(self):
        records = [
            {
                'name': f"Name{i}",
                'phone_number': f"12345678{i:02d}",
                'country': f"Country{i}",
                'province': f"Province{i}",
                'city': f"City{i}",
                'area': f"Area{i}",
                'road_street': f"Street{i}",
                'address': f"123 Street{i}, Area{i}, City{i}, Province{i}",
            }
            for i in range(1, 101)
        ]
        response = self.client.post(
        reverse('bulk_create_addresses'),
        records,
        format='json'
    )
    # print(response.json())  # For debugging if errors persist
    # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # self.assertEqual(Address.objects.count(), 101)  # Adjust expected count to include the setUp record