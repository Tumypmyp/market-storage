from django.contrib import admin
from .models import Order

from django.urls import reverse
from django.http import HttpResponseRedirect
import requests



class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # editing an existing order
            readonly_fields += ('name', 'status',)
        return readonly_fields

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model() method to save the object
        super().save_model(request, obj, form, change)
        
        # Send API request to the other server
        api_url = 'http://localhost:8001/api/order/add/'
        data = {
            'name': obj.name,
            'status': obj.status,
        }
        response = requests.post(api_url, data=data, verify=False)

        # Redirect back to the change list view
        return HttpResponseRedirect(reverse('admin:example_order_changelist'))


admin.site.register(Order, OrderAdmin)