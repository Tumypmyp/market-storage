from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import Order
from .serializer import OrderSerializer

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdate(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'