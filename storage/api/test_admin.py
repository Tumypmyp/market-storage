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
        self.order = Order.objects.create(name='Test Order', status='NEW', id=1)
        self.admin = OrderAdmin(Order, self.site)

    def test_save_model(self):
        api_url = 'http://market:8000/api/order/update/1/'
        data = {'id': 1, 'name': 'New Order Name', 'status': Order.COMPLETED}

        # Mock the API endpoint
        with requests_mock.Mocker() as m:
            m.put(api_url, json=data)
            
            obj = self.order
            obj.name = 'New Order Name'
            obj.status = 'COMPLETED'
            response = self.admin.save_model(MagicMock(), obj, None, None)
            
            self.assertEqual(m.call_count, 1)
            self.assertEqual(m.last_request.url, api_url)
            self.assertEqual(m.last_request.method, 'PUT')
            self.assertEqual(m.last_request.body, 'id=1&name=New+Order+Name&status=COMPLETED')