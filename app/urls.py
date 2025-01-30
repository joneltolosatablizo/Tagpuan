from django.urls import path
from .views import (HomePageView, AboutPageView, OrderListView,
                    OrdersDetailView, OrderCreateView, OrderUpdateView,
                    OrderDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('order/', OrderListView.as_view(), name='order'),
    path('order/<int:pk>', OrdersDetailView.as_view(), name='order_detail'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete', OrderDeleteView.as_view(), name='order_delete'),
]