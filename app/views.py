from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Order, Category, Product
from django.urls import reverse_lazy
from .models import  Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserOrder, SavedCarts


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
    template_name = 'app/review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'app/review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['feedback']
    template_name = 'app/review_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['feedback']
    template_name = 'app/review_update.html'

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'app/review_delete.html'
    success_url = reverse_lazy('review_list')


def cart(request):
    if request.user.is_authenticated:
        return render(request, "app/cart.html")
    else:
        return redirect("app/registration:login")

def checkout(request):
    if request.method == 'POST':
        cart = json.loads(request.POST.get('cart'))
        price = request.POST.get('price_of_cart')
        username = request.user.username
        response_data = {}
        list_of_items = [item["item_description"] for item in cart]

        order = UserOrder(username=username, order=list_of_items, price=float(price), delivered=False) #create the row entry
        order.save() #save row entry in database

        response_data['result'] = 'Order Recieved!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def view_orders(request):
    if request.user.is_superuser:
        #make a request for all the orders in the database
        rows = UserOrder.objects.all().order_by('-time_of_order')
        #orders.append(row.order[1:-1].split(","))

        return render(request, "app/orders.html", context = {"rows":rows})
    else:
        rows = UserOrder.objects.all().filter(username = request.user.username).order_by('-time_of_order')
        return render(request, "app/orders.html", context = {"rows":rows})

def mark_order_as_delivered(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        UserOrder.objects.filter(pk=id).update(delivered=True)
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def save_cart(request):
    if request.method == 'POST':
        cart = request.POST.get('cart')
        saved_cart = SavedCarts(username=request.user.username, cart=cart) #create the row entry
        saved_cart.save() #save row entry in database
        return HttpResponse(
            json.dumps({"good":"boy"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def retrieve_saved_cart(request):
    try:
        saved_cart = SavedCarts.objects.get(username = request.user.username)
        return HttpResponse(saved_cart.cart)
    except:
        return HttpResponse('')

class ProfileUpdate(UpdateView):
    model = get_user_model()
    fields = ['username', 'email', 'profile_pic']
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('Profile')