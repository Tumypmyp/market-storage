from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
from django.http import HttpResponseRedirect
from unittest.mock import patch, MagicMock
import requests_mock
import json

from .admin import OrderAdmin
from .models import Order

class OrderAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.order = Order.objects.create(name='Test Order', status=Order.NEW, id=1)
        self.admin = OrderAdmin(Order, self.site)

    def test_save_model(self):
        api_url = 'http://storage:8000/api/order/add/'
        data = {'id': 1, 'name': 'Test Order', 'status': Order.NEW}

        # Mock the API endpoint
        with requests_mock.Mocker() as m:
            m.post(api_url, json=data)
                
            obj = self.order
            response = self.admin.save_model(MagicMock(), obj, None, None)
            
            self.assertEqual(m.call_count, 1)
            self.assertEqual(m.last_request.url, api_url)
            self.assertEqual(m.last_request.method, 'POST')
            self.assertEqual(m.last_request.body, 'id=1&name=Test+Order&status=new')
