from django.test import TestCase
from .models import Order

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(name='Test Order', status=Order.NEW, id=3)
    
    def test_order_str_method(self):
        self.assertEqual(str(self.order), 'Test Order (New) #3')
