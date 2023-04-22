from django.contrib import admin
from .models import Order

from django.urls import reverse
from django.http import HttpResponseRedirect
import requests



class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )

    def save_model(self, request, obj, form, change):
        # Call the parent class's save_model() method to save the object
        super().save_model(request, obj, form, change)
        
        # Send API request to the other server
        api_url = f'http://localhost:8000/api/order/update/{obj.id}/'
        data = {
            'id' : id,
            'name': obj.name,
            'status': obj.status,
        }
        response = requests.put(api_url, data=data)

        # Redirect back to the change list view
        return HttpResponseRedirect(reverse('admin:api_order_changelist'))


admin.site.register(Order, OrderAdmin)