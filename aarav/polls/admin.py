from django.contrib import admin
from .  models import Questions,Choice,Answer
# Register your models here.
admin.site.register(Questions)
admin.site.register(Choice)
admin.site.register(Answer)