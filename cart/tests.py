from django.test import TestCase, Client
from django.urls import reverse
from cart.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.add_url = reverse('add')
        self.product_data = {
            'shape': 'Oval',
            'size': '25',
            'location': 'Mumbai',
            'price': 5620
        }

    def test_add_product(self):
        response = self.client.post(self.add_url, self.product_data)
        print(response)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(shape="Oval", size="25", location="Mumbai", price=5620).exists())
