from django.contrib import admin
from .models import ClothType,Customer,ServiceType,ServicePrice,CustomerOrder,CustomerOrderDetails
# Register your models here.
admin.site.register(ClothType)
admin.site.register(ServiceType)
admin.site.register(ServicePrice)
admin.site.register(Customer)
admin.site.register(CustomerOrder)
admin.site.register(CustomerOrderDetails)