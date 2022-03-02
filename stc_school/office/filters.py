from django.db.models.fields import DateField
import django_filters
from django_filters.filters import DateFilter
from accounts.models import Teacher
from home.models import Class_list
from django import forms


class Class_listFilter(django_filters.FilterSet):

    class Meta:
        model = Class_list
        fields = ['session_year',]