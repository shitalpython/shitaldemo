
from django.urls import path
from . views import CustomerDetailsview,Customerorder

urlpatterns = [
      path('',CustomerDetailsview.as_view(),name='cms'),
      path('<int:id>/Customerorder',Customerorder,name='customerorder')

]
