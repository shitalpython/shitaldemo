from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import dispatcher,receiver

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=20,null=False,blank=False)
    salary=models.IntegerField(null=True,blank=True)
    class Meta:
        ordering=('-salary',)

    def __str__(self):
        return "{0}".format(self.user.first_name)

@receiver(post_save,sender=User)
def user_iscreated(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()