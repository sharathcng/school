from django.forms.widgets import DateInput
from assessments.models import Assessment, Assessment_type
from django import forms
from home.models import Class_list, Session_year


class AssessmentCreationForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'assessment_type',
            'class_name',
            'subject',
            'date',
            'start_time',
            'end_time',
        ]

        widgets = {
            'date': DateInput(attrs={'class': 'form-control','type':'date'}, format='%Y-%m-%d'),
            'start_time': DateInput(attrs={'class': 'form-control','type':'time'}, format='T%H:%M'),
            'end_time': DateInput(attrs={'class': 'form-control','type':'time'}, format='T%H:%M'),
        }
    

    def __init__(self, *args, **kwargs):
        super(AssessmentCreationForm,self).__init__(*args, **kwargs)
        self.fields['assessment_type'].queryset = Assessment_type.objects.filter(session_year = Session_year.objects.last())
        self.fields['class_name'].queryset = Class_list.objects.filter(session_year = Session_year.objects.last())



class AssessmentTypeCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssessmentTypeCreationForm,self).__init__(*args, **kwargs)
        self.fields['session_year'].queryset = Session_year.objects.all()

    class Meta:
        model = Assessment_type
        fields = [
            'session_year',
            'assessment_name',
            'assessment_description',
            'start_date',
            'end_date',
        ]

        widgets = {
            'session_year' : forms.Select(attrs={'class': 'form-control'}),
            'assessment_name' : forms.Select(attrs={'class': 'form-control'}),
            'assessment_description' : forms.Textarea(attrs={'class': 'form-control', 'rows' : 2}),
            'start_date': DateInput(attrs={'class': 'form-control','type':'date'}, format='%Y-%m-%d'),
            'end_date': DateInput(attrs={'class': 'form-control','type':'date'}, format='%Y-%m-%d'),
        }
