from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
from django.http import HttpResponseRedirect
from unittest.mock import patch, MagicMock
import requests_mock

from .admin import OrderAdmin
from .models import Order

class OrderAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.order = Order.objects.create(name='Test Order', status='NEW')
        self.admin = OrderAdmin(Order, self.site)

    def test_save_model(self):
        api_url = 'http://localhost:8000/api/order/update/1/'
        expected_data = {'id': 1, 'name': 'New Order Name', 'status': 'COMPLETED'}

        # Mock the API endpoint
        with requests_mock.Mocker() as m:
            m.put(api_url, json=expected_data)
            
            # Call the save_model function
            request = MagicMock()
            obj = self.order
            obj.name = 'New Order Name'
            obj.status = 'COMPLETED'
            response = self.admin.save_model(request, obj, None, None)

            # print(m.last_request.body)
            
            # Print out the response content
            # response_content = response.content.decode('utf-8')
            # print(f'Response content: {response_content}')

            # Assert that the API was called with the correct data    
            self.assertEqual(m.call_count, 1)
            self.assertEqual(m.last_request.url, api_url)
            self.assertEqual(m.last_request.method, 'PUT')
            self.assertEqual(m.last_request.json(), expected_data)
