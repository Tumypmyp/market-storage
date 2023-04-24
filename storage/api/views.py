from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Order
from .serializer import OrderSerializer

class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'