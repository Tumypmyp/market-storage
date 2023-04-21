from django.urls import path

from . import views

urlpatterns = [
    path("order/", views.OrderList.as_view(), name='order-list'),
    path("order/add/", views.OrderCreate.as_view(), name='order-create'),
    ]
