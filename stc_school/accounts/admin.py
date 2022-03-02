from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.forms import TeacherCreationForm, CustomUserChangeForm
from accounts.models import Staff, Student, Parents_detail, Teacher, CustomUser

# Register your models here.


class Student_inline(admin.TabularInline):
    model = Student

class Teacher_inline(admin.TabularInline):
    model = Teacher

class Parent_inline(admin.TabularInline):
    model = Parents_detail


class CustomUserAdmin(UserAdmin):
    add_form = TeacherCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # ordering = ('email',)
    list_display = ('username', 'is_active')
    list_filter = ('is_superuser','role')
    fieldsets = (
        (None, {
            "fields": (
                'username', 'password','role',
            ),
        }),
        ('Permissions', {
            "classes": (),
            "fields": (
                'is_active', ('is_superuser','is_classTeacher')
            ),
        }),
        ('Important Dates', {
            "classes": ('collapse',),
            "fields": (
                'last_login', 'date_joined'
            ),
        }),
        ('Advanced Options', {
            "classes": ('collapse',),
            "fields": (
                'groups', 'user_permissions'
            ),
        })
    )

    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": (
                'username', 'password1', 'password2', 'is_active', 'is_superuser','is_classTeacher', 'groups'
            ),
        }),
    )
    # inlines = [
    #     Student_inline,
    #     Teacher_inline,
    # ]


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('user_id','full_name', 'current_class', )
    list_filter = ('gender',)
    inlines = [
        Parent_inline,
    ]

class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('user_id', 'full_name', 'gender',)
    list_filter = ('gender',)

class StaffAdmin(admin.ModelAdmin):
    model = Staff
    list_display = ('user_id', 'full_name', 'gender',)
    list_filter = ('gender',)

class ParentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('student_id', 'father_name', 'mother_name',)
    # list_filter = ('gender',)

#admin.site.unregister(User)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parents_detail, ParentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Staff, StaffAdmin)
