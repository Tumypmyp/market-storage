from django.test import TestCase
from .models import Order

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(name='Test Order', status='NEW')
    
    def test_order_str_method(self):
        self.assertEqual(str(self.order), 'Test Order (New)')
    
    def test_order_status_choices(self):
        status_choices = dict(self.order.STATUS_CHOICES)
        self.assertEqual(status_choices['NEW'], 'New')
        self.assertEqual(status_choices['IN_PROCESS'], 'In Process')
        self.assertEqual(status_choices['COMPLETED'], 'Completed')
