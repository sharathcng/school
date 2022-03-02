from django.contrib import admin
from assessments.models import Assessment_type, Assessment, Result

# Register your models here.

admin.site.register(Assessment_type)
admin.site.register(Assessment)
admin.site.register(Result)