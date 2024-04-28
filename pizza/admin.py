from django.contrib import admin
from .models import PizzaItem, BasketItem, UserTG

# Register your models here.

admin.site.register(PizzaItem)
admin.site.register(BasketItem)
admin.site.register(UserTG)
