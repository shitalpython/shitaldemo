from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager


# Create your models here.
class CustomerManager(models.Manager):
    def all_cutomer(self):
        return Customer.objects.all()


class Customer(models.Model):
    name=models.CharField(max_length=100,null=False)
    contactno=models.CharField(max_length=13,null=False)
    altcontactno=models.CharField(max_length=13,null=True,blank=True)
    address=models.TextField(max_length=250,null=True)
    createdby=models.ForeignKey(User,on_delete=models.CASCADE)
    createddate=models.DateTimeField(auto_now_add=True)
    updateddate=models.DateTimeField(auto_now=True)

    objects=CustomerManager()

    def __str__(self):
        return self.name


class ClothType(models.Model):
    clothtype=models.CharField(max_length=100)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clothtype

class ServiceType(models.Model):
    servicetype = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True,blank=True)
    updateddate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.servicetype


class ServicePrice(models.Model):
    clothtype=models.ForeignKey(ClothType,on_delete=models.CASCADE,null=False)
    servicetype=models.ForeignKey(ServiceType,on_delete=models.CASCADE,null=False)
    serviceprice=models.FloatField(null=False)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.clothtype)


class CustomerOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(order_status='Incoming')

    def hn(request):
        return CustomerOrder.objects.select_related().filter(order_status='Incoming')

    def unn(self):
        z=Customer.objects.all()
        q=Customer.objects.all()
        w=CustomerOrder.objects.all()
        return z.union(q,w)

class CustomerOrder(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_in_date=models.DateTimeField(auto_now_add=True,null=False,editable=False)
    order_out_date=models.DateTimeField(null=True)
    total_bill=models.FloatField(null=True,default=0,editable=False)
    advance=models.FloatField(null=True,default=0)
    balance=models.FloatField(null=False,default=0,editable=False)
    cloth_quantity=models.IntegerField(null=True,default=0,editable=False)
    billstatus=models.BooleanField(max_length=20,null=False,default=0,editable=False)
    order_status=models.CharField(max_length=20,null=False,default='Incoming',editable=False)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True,editable=False)
    updateddate = models.DateTimeField(auto_now=True,editable=False)

    objects=CustomerOrderManager()

    def __str__(self):
        return str(self.customer)


class CustomerOrderDetails(models.Model):
    customer_order=models.ForeignKey(CustomerOrder,on_delete=models.CASCADE,null=False)
    serviceprice=models.ForeignKey(ServicePrice,on_delete=models.CASCADE,null=False)
    quntity=models.IntegerField(null=False)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer_order)
