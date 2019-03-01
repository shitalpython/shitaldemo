
from django.urls import path
from . import views

urlpatterns = [
      path('', views.index,name='polls_list'),
      path('<int:id>/details/', views.details,name='polls_details'),
      path('<int:id>/', views.poll,name='poll'),

]
