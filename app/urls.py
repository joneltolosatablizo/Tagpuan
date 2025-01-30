from django.urls import path
from .views import (HomePageView, AboutPageView, OrderListView)
from .views import (OrdersDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView)
from .views import (ReviewCreateView, ReviewDeleteView,ReviewDetailView, ReviewListView, ReviewUpdateView)
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



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

    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("view-orders", views.view_orders, name="view_orders"),
    path("mark_order_as_delivered", views.mark_order_as_delivered, name="mark_order_as_delivered"),
    path("save_cart", views.save_cart, name="save_cart"),
    path("retrieve_saved_cart", views.retrieve_saved_cart, name="retrieve_saved_cart"),
]