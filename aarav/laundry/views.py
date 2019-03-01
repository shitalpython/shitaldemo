from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer,CustomerOrder
class CustomerDetailsview(ListView):
    template_name = "polls/customerdetails.html"
    context_object_name = 'customer_list'
    def get_queryset(self):
        return CustomerOrder.objects.hn()



def Customerorder(request,id='NULL'):
    context={}
    customerobj=Customer.objects.get(id=id)
    context['customerobj']=customerobj
    return render(request,'polls/customerorder.html',context)
