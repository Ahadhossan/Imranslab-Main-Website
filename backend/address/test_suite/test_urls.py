from django.test import SimpleTestCase
from django.urls import reverse, resolve
from address.views import address_list, create_address, update_address, delete_address

class TestUrls(SimpleTestCase):
    def test_address_list_url(self):
        url = reverse('address_list')
        self.assertEqual(resolve(url).func, address_list)

    def test_create_address_url(self):
        url = reverse('create_address')
        self.assertEqual(resolve(url).func, create_address)

    def test_update_address_url(self):
        url = reverse('update_address', args=[1])
        self.assertEqual(resolve(url).func, update_address)

    def test_delete_address_url(self):
        url = reverse('delete_address', args=[1])
        self.assertEqual(resolve(url).func, delete_address)
