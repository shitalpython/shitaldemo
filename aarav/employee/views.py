from django.shortcuts import render
from django.http import HttpResponse
from  django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return HttpResponse("hellow  from python")


class ProfileUpdate(UpdateView):
    fields = ['designation','salary']
    template_name = 'polls/profileupd.html'
    success_url = reverse_lazy('employee_home')
    def get_object(self):
        return self.request.user.profile


class ProfileDetails(DetailView):
    template_name = 'polls/empdetails.html'
    def get_object(self):
        return self.request.user.profile

