from django.urls import path

from . import views

urlpatterns = [
    path("", views.OrderList.as_view()),
    path("add/", views.OrderCreate.as_view()),
    ]
