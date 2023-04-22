from django.urls import path

from . import views

urlpatterns = [
    path("order/", views.OrderList.as_view()),
    path('order/update/<int:id>/', views.OrderUpdate.as_view(), name='order-update'),
    ]
