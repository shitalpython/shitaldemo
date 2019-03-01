from django.db import models
from django.contrib.auth.models import User
from django.db.models import Manager
# Create your models here.
class Questions(models.Model):
    title=models.TextField(null=True,blank=True)
    status=models.CharField(default='Deactive',max_length=10)
    startdate=models.DateTimeField(null=True,blank=True)
    enddate=models.DateTimeField(null=True,blank=True)
    createdby=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

    @property
    def choice(self):
        return self.choice_set.all()



    def __str__(self):
        return '{}{}{}'.format(self.title,' ' ,self.status)

class Choice(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    text=models.TextField(null=True,blank=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    @property
    def votes(self):
        return self.answer_set.count()

    def __str__(self):
        return self.text


class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Choice=models.ForeignKey(Choice,on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name+' '+self.Choice.text