from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from .models import Order, OrderItem

def order_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail',
                                                  args=[obj.id]))
order_detail.allow_tags = True

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'first_name',
                    'last_name',
                    'email',
                    'address',
                    'postal_code',
                    'city',
                    'paid',
                    'created',
                    'updated',
                    order_detail,
                    order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)
