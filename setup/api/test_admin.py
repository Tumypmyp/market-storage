from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.models import Order
from unittest.mock import patch


class OrderAdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='password', email='admin@example.com')
        self.client.force_login(self.user)
        self.order = Order.objects.create(name='Test Order', status='New')

    def test_save_model_sends_api_request(self):
        with patch('requests.post') as mock_post:
            url = reverse('admin:myapp_order_change', args=[self.order.id])
            data = {'name': 'Updated Order', 'status': 'Completed'}
            response = self.client.post(url, data, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Order was changed successfully.')

            mock_post.assert_called_once_with('http://localhost:8001/api/order/add/',
                                              data={'name': 'Updated Order', 'status': 'Completed'},
                                              verify=False)
