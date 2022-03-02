from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager

gender_choices = (
    (1,"Male"),
    (2,"Female"),
    (3,"Other")
)

role_choices = (
    (1,"Student"),
    (2,"Teacher"),
    (3,"Staff"),
)

blood_choices = (
    ('O+',"O+"),
    ('O-',"O-"),
    ('A+',"A+"),
    ('A-',"A-"),
    ('B+',"B+"),
    ('B-',"B-"),
    ('AB+',"AB+"),
    ('AB-',"AB-"),
    ('Not Sure',"Not Sure")
)

#Custom User Model
class CustomUser(AbstractUser):
    email = None
    first_name = None
    last_name = None
    role = models.PositiveIntegerField(choices = role_choices, null=True)
    is_classTeacher = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    


#Student Model
class Student(models.Model):
    user_id = models.OneToOneField(CustomUser,primary_key=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)
    place_of_birth = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(choices = gender_choices, null=True)
    email_id = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=10, choices = blood_choices, null=True)
    aadhaar_number = models.CharField(max_length=12, blank=True, null=True)
    present_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    started_class = models.CharField(max_length=255,blank=True, null=True)
    current_class = models.ForeignKey("home.Class_list",on_delete=models.CASCADE,related_name='current_class')
    joining_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

#parents details Model
class Parents_detail(models.Model):
    student_id = models.OneToOneField(Student,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=255)
    father_qualification = models.CharField(max_length=255)
    mother_qualification = models.CharField(max_length=255)

#Teacher Model
class Teacher(models.Model):
    user_id = models.OneToOneField(CustomUser,primary_key=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    gender = models.IntegerField(choices = gender_choices, blank=True, null=True)
    email_id = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=10, choices = blood_choices, null=True, blank=True)
    aadhaar_number = models.CharField(max_length=255, blank=True, null=True)
    present_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True, null=True)
    started_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    handling_subjects = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['user_id']
    

    def __str__(self):
        return self.full_name


#Staff Model
class Staff(models.Model):
    user_id = models.OneToOneField(CustomUser,primary_key=True,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    gender = models.IntegerField(choices = gender_choices, blank=True, null=True)
    email_id = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    blood_group = models.CharField(max_length=10, choices = blood_choices, null=True, blank=True)
    aadhaar_number = models.CharField(max_length=255, blank=True, null=True)
    present_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,blank=True, null=True)
    started_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['user_id']
    

    def __str__(self):
        return self.full_name