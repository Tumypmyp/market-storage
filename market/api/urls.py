from django.urls import path

from . import views

urlpatterns = [
    path("order/", views.OrderList.as_view(), name='order-list'),
    path('order/update/<int:id>/', views.OrderUpdate.as_view(), name='order-update'),
    ]
