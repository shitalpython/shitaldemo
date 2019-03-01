from django import forms
from . models import CustomerOrder,CustomerOrderDetails

class CustomerOrderForm(forms.ModelForm):
    customer=forms.S