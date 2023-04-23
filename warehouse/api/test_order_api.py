from .models import Order
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class OrderTests(APITestCase):
    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
    
    def test_create_order(self):
        url = reverse('order-create')
        data = {'name': 'Test Order', 'status': 'NEW'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.json()
        self.assertEqual(response_data['name'], 'Test Order')
        self.assertEqual(response_data['status'], 'NEW')
        
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().name, 'Test Order')

        
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['name'], 'Test Order')
        self.assertEqual(response_data[0]['status'], 'NEW')



        
