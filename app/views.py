from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Order, Category, Product
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

    def directions(request):
        if request.user.is_authenticated:
            return render(request, "app/about.html")
        else:
            return redirect("registration/login.html")

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'app/order_list.html'


class OrdersDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['user','created_at', 'your_order', 'status']
    template_name = 'app/order_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        context['categorys'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['user','created_at','your_order', 'status']
    template_name = 'app/order_update.html'

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'app/order_delete.html'
    success_url = reverse_lazy('order')


