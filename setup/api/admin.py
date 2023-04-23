from django.contrib import admin
from .models import Order

from django.urls import reverse
from django.http import HttpResponseRedirect
import requests



class OrderAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # editing an existing order
            readonly_fields += ('id', 'name', 'status',)
        return readonly_fields

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model() method to save the object
        super().save_model(request, obj, form, change)
        
        # Send API request to the other server
        api_url = 'http://storage:8000/api/order/add/'
        data = {
            'id' : obj.id,
            'name': obj.name,
            'status': obj.status,
        }
        
        try:
            response = requests.post(api_url, data=data, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Show warning message if the API call failed
            self.message_user(request, 'Warning: Failed to update order on storage side: {}'.format(str(e)), level='warning')


admin.site.register(Order, OrderAdmin)