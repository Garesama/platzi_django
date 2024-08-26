from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductoInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductoInlineAdmin
    ]


admin.site.register(Order, OrderAdmin)