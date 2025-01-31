from django.contrib import admin
from .models import UserProfile
from .models import Category
from .models import Product
from .models import Order
from .models import Orderitem
from .models import UserOrder
from .models import SavedCarts




admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)