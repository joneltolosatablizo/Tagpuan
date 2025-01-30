from django.contrib import admin
from .models import UserProfile
from .models import Category
from .models import Product
from .models import Order
from .models import Orderitem




admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderitem)