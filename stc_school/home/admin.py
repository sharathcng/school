from django.contrib import admin
from home.models import Session_year, Class_list, Subject, Teacher_allocation

# Register your models here.

class SessionAdmin(admin.ModelAdmin):
    model = Session_year
    list_display = ('sessionYear','start_date','end_date', )

class ClassesAdmin(admin.ModelAdmin):
    model = Class_list
    list_display = ('session_year','class_name', 'class_section')

admin.site.register(Session_year,SessionAdmin)
admin.site.register(Class_list,ClassesAdmin)
admin.site.register(Subject)
admin.site.register(Teacher_allocation)