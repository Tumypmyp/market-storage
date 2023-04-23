from django.contrib import admin
from .models import Order

from django.urls import reverse
from django.http import HttpResponseRedirect
import requests



class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'name', )

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model() method to save the object
        super().save_model(request, obj, form, change)
        
        # Send API request to the other server
        api_url = f'http://market:8000/api/order/update/{obj.id}/'
        data = {
            'id' : obj.id,
            'name': obj.name,
            'status': obj.status,
        }
        
         
        try:
            response = requests.put(api_url, data=data, verify=False)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Show warning message if the API call failed
            self.message_user(request, 'Warning: Failed to update order on storage side: {}'.format(str(e)), level='warning')

admin.site.register(Order, OrderAdmin)