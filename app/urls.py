from django.urls import path
from .views import (HomePageView, AboutPageView, OrderListView)
from .views import (OrdersDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView)
from .views import (ReviewCreateView, ReviewDeleteView,ReviewDetailView, ReviewListView, ReviewUpdateView)



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('order/', OrderListView.as_view(), name='order'),
    path('order/<int:pk>', OrdersDetailView.as_view(), name='order_detail'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete', OrderDeleteView.as_view(), name='order_delete'),
    path('review/', ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('review/create', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/edit', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete'),
]