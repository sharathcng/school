from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import CustomUser, Staff
from django import forms
from accounts.models import Student, Teacher
import math

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'role',
        ]
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(StudentCreationForm, self).__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs["class"] = "form-control"
        self.fields['password2'].widget.attrs["class"] = "form-control"


class StaffCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'role',
        ]

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(StaffCreationForm, self).__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs["class"] = "form-control"
        self.fields['password2'].widget.attrs["class"] = "form-control"


class TeacherCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'role',
        ]

        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TeacherCreationForm, self).__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs["class"] = "form-control"
        self.fields['password2'].widget.attrs["class"] = "form-control"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'role',
        ]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user_id']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'present_address': forms.Textarea(attrs={'rows': 3}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'started_class': forms.Select(attrs={'class': 'form-select'}),
            'current_class': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['user_id']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'started_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'present_address': forms.Textarea(attrs={'rows': 3}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateTeacherForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False

class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user_id']
        widgets = {
            'full_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email_id' : forms.EmailInput(attrs={'class':'form-control', 'type': 'email'}),
            'phone_number' : forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'started_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'present_address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'aadhaar_number' : forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }
    def clean_aadhaar_number(self):
            data = int(self.cleaned_data['aadhaar_number'])
            if data == "":
                raise forms.ValidationError("This field cannot be empty")
            if math.floor(math.log10(data))+1 != 12:
                digit = math.floor(math.log10(data))+1
                raise forms.ValidationError("Aadhaar number is always 12 digit, you have entered "+str(digit)+" digit. Please enter correct Aadhaar Number")
            for instance in Staff.objects.all():
                if int(instance.aadhaar_number) == data and instance.full_name != self.cleaned_data['full_name']:
                    raise forms.ValidationError("Aadhaar Number with "+str(data)+" is already registered with a name - "+instance.full_name+". Please enter the correct Aadhaar Number")
                return data

    def __init__(self, *args, **kwargs):
        super(UpdateStaffForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False
    
    
