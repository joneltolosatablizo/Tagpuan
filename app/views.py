from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Order, Category, Product
from django.urls import reverse_lazy
from .models import  Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_orders = Order.objects.filter(your_order__icontains=query)
        else:
            filtered_orders = Order.objects.all()
        context['orders'] = filtered_orders
        return context

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


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'app/reviews/review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'app/reviews/review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['feedback']
    template_name = 'app/reviews/review_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['feedback']
    template_name = 'app/reviews/review_update.html'

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'app/reviews/review_delete.html'
    success_url = reverse_lazy('review_list')


