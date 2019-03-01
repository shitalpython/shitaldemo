from django.shortcuts import render
from .models import *
from django.http import HttpResponse
def index(request):
    context={}
    questions=Questions.objects.all()
    context['title']='polls'
    context['questions']=questions
    return render(request,'polls/index.html',context)

def details(request,id="NULL"):
    context={}
    questions=Questions.objects.get(id=id)
    context['title']='polls'
    context['questions']=questions
    return render(request,'polls/details.html',context)



def poll(request,id="NULL"):
    if request.method == 'GET':
        context = {}
        questions = Questions.objects.get(id=id)
        context['title'] = 'polls'
        context['questions'] = questions
        return render(request,'polls/poll.html',context)

    if request.method =="POST":
        user_id=1
        data=request.POST
        ret= Answer.objects.create(user_id=user_id,choice_id=data['answer'])
        if ret:
           return HttpResponse("successfully")
        else:
            return HttpResponse("NOT successfully")