from django.db.models.fields import DateField
import django_filters
from django_filters.filters import DateFilter
from accounts.models import Staff, Teacher
from home.models import Class_list
from django import forms

#filter for teachers
class TeachersFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="started_date",  label='Start Date', lookup_expr='gte',widget=forms.DateInput(attrs={'class':'form-control ','type':'date'}))
    end_date = DateFilter(field_name="end_date", label='End Date', lookup_expr='lte',widget=forms.DateInput(attrs={'class':'form-control ','type':'date'}))
    

    class Meta:
        model = Teacher
        fields = []

class StaffsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="started_date",  label='Start Date', lookup_expr='gte',widget=forms.DateInput(attrs={'class':'form-control ','type':'date'}))
    end_date = DateFilter(field_name="end_date", label='End Date', lookup_expr='lte',widget=forms.DateInput(attrs={'class':'form-control ','type':'date'}))
    

    class Meta:
        model = Staff
        fields = []