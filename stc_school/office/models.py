from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from accounts.models import Student

from home.models import Class_list

# Create your models here.
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    class_name  = models.ForeignKey(Class_list, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    morng_presence = models.BooleanField(default=True)
    aftrn_presence = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    