from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Address


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
            address="Shop 1, 1 George Street"
        )

    def test_address_creation(self):  # Test the model
        self.assertEqual(self.address.city, "Sydney")
        self.assertEqual(self.address.name, "John Doe")

    def test_address_str_method(self):  # Test the __str__ method
        self.assertEqual(str(self.address), "John Doe - Sydney, Central Business District")


class AddressViewTest(TestCase):  # Test the views

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
            address="Shop 1, 1 Collins Street"
        )

    def test_update_address_view(self):  # Test the PUT request
        response = self.client.post(reverse('update_address', args=[self.address.id]), {

            'name': "Jane Doe",
            'phone_number': "0423456789",
            'country': "Australia",
            'province': "VIC",
            'city': "Melbourne",
            'area': "Docklands",
            'road_street': "Collins Street",
            'address': "Shop 1, 1 Collins Street"
        })
        self.assertEqual(response.status_code, 302)
        self.address.refresh_from_db()

    def test_delete_address_view(self):  # Test the DELETE request
        response = self.client.post(reverse('delete_address', args=[self.address.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Address.objects.filter(id=self.address.id).exists())


class AddressAPITest(TestCase):  # Test the API endpoints
    def setUp(self):  # Create an address object
        self.client = APIClient()
        self.address = Address.objects.create(
            name="Bob Doe",
            phone_number="0445678901",
            country="Australia",
            province="WA",
            city="Perth",
            area="CBD",
            road_street="Hay Street",
            address="Shop 1, 1 Hay Street"
        )

    def test_get_addresses(self):  # Test the GET request
        response = self.client.get(reverse('address-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the status code is 200
        self.assertGreaterEqual(len(response.data), 1)  # Check if the response contains at least one address

    def test_create_address_api(self):  # Test the POST request
        response = self.client.post(
            reverse('address-list'),
            {
                'name': "Clara Doe",
                'phone_number': "0456789012",
                'country': "Australia",
                'province': "SA",
                'city': "Adelaide",
                'area': "Glenelg",
                'road_street': "Jetty Road",
                'address': "Shop 1, 1 Jetty Road",
            },
            # why format telling is important?
            # https://www.django-rest-framework.org/api-guide/requests/#format
            format='json'  # Ensure the data is sent as JSON

        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if the status code is 201
        self.assertEqual(Address.objects.last().name,
                         "Clara Doe")  # check if the last created address has the correct name

    def test_update_address_api(self):  # Test the PUT request
        response = self.client.put(reverse('address-detail', args=[self.address.id]), {
            'name': "Bob Doe",
            'phone_number': "0445678901",
            'country': "Australia",
            'province': "WA",
            'city': "Perth",
            'area': "CBD",
            'road_street': "Hay Street",
            'address': "Shop 1, 1 Hay Street",
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()  # Refresh the object from the database

    def test_delete_address_api(self):  # Test the DELETE request
        response = self.client.delete(reverse('address-detail', args=[self.address.id]))  # Send a DELETE request
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Check if the status code is 204
        self.assertFalse(Address.objects.filter(id=self.address.id).exists())  # Check if the address was deleted
