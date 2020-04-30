from django.contrib import admin

# Register your models here.
from .models import order, ConfirmOrder

admin.site.register(order)
admin.site.register(ConfirmOrder)