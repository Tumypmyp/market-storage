from .models import Order
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class OrderTests(APITestCase):
    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_order(self):
        url = reverse('order-create')
        data = {'name': 'Test Order', 'status': 'NEW'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().name, 'Test Order')
