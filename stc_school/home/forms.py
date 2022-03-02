from tkinter.tix import Select
from django import forms
from django.forms.widgets import DateInput, TextInput
from home.models import Class_list, Session_year, Subject, Teacher_allocation
from accounts.models import Teacher
from django.core.exceptions import NON_FIELD_ERRORS

class ClassCreationForm(forms.ModelForm):
    class Meta:
        model = Class_list
        fields = [
            'session_year',
            'class_name',
            'class_section',
            'class_teacher',
        ]

        widgets = {
            'session_year': forms.Select(attrs={'class': 'form-select'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_section': forms.TextInput(attrs={'class': 'form-control'}),
            'class_teacher': forms.Select(attrs={'class': 'form-select'}),


        }
    

    def __init__(self, *args, **kwargs):
        super(ClassCreationForm,self).__init__(*args, **kwargs)
        self.fields['class_teacher'].queryset = Teacher.objects.filter(end_date = None)


class BatchCreationForm(forms.ModelForm):
    class Meta:
        model = Session_year
        fields = [
            'sessionYear',
            'start_date',
            'end_date',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}, format='%Y-%m-%d'),
        }

class SubjectCreationForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'subject_name',
        ]

        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']
        widgets = {
            'subject_name' : forms.TextInput(attrs={'class':'form-control'}),
        }

class UpdateClassForm(forms.ModelForm):
    class Meta:
        model = Class_list
        fields = '__all__'
        widgets = {
            'session_year' : forms.Select(attrs={'class':'form-select'}),
            'class_name' : forms.TextInput(attrs={'class':'form-control'}),
            'class_section' : forms.TextInput(attrs={'class':'form-control'}),
            'class_teacher' : forms.Select(attrs={'class':'form-select'}),
        }


class TeacherAllocationCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher_allocation
        fields = [
            'session_year',
            'class_name',
            'subject',
            'teacher',
        ]

        widgets = {
            'session_year': forms.Select(attrs={'class': 'form-select','disabled':'disabled'}),
            'class_name': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'teacher': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super(TeacherAllocationCreationForm,self).__init__(*args, **kwargs)
        self.fields['class_name'].queryset = Class_list.objects.filter(session_year = Session_year.objects.last())
        self.fields['session_year'].initial = Session_year.objects.last()

class TeacherAllocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher_allocation
        fields = [
            'session_year',
            'class_name',
            'subject',
            'teacher',
        ]

        widgets = {
            'session_year': forms.Select(attrs={'class':'form-select','disabled':'disabled'}),
            'class_name': forms.Select(attrs={'class': 'form-select','disabled':'disabled'}),
            'subject': forms.Select(attrs={'class': 'form-select','disabled':'disabled'}),
            'teacher': forms.Select(attrs={'class': 'form-select'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(TeacherAllocationUpdateForm,self).__init__(*args, **kwargs)
    #     current_object = Teacher_allocation.objects.get(id = self.kwargs['pk'])
    #     self.fields['session_year'].initial = current_object.session_year
    #     self.fields['class_name'].initial = current_object.class_name