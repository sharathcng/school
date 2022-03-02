from django.db import models
from django.db.models.fields import AutoField
from django.core.exceptions import ValidationError
from django.utils import timezone

assessment_choices = (
    ('Monthly Test - 1',"Monthly Test - 1"),
    ("Monthly Test - 2","Monthly Test - 2"),
    ("Midterm Exam","Midterm Exam"),
    ("Monthly Test - 3","Monthly Test - 3"),
    ("Monthly Test - 4","Monthly Test - 4"),
    ("Final Exam","Final Exam"),
)

# Assessment_type Model
class Assessment_type(models.Model):
    id = models.AutoField(primary_key=True)
    session_year = models.ForeignKey("home.Session_year",on_delete=models.CASCADE)
    assessment_name = models.CharField(max_length=255, choices = assessment_choices)
    assessment_description = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('session_year','assessment_name'),)

    def __str__(self):
        return self.assessment_name

class Assessment(models.Model):
    def validate_date(date):
        if date < timezone.now().date():
            raise ValidationError("Please select date from today onwards.")

    id = models.AutoField(primary_key=True)
    assessment_type = models.ForeignKey("assessments.Assessment_type",on_delete=models.CASCADE)
    class_name = models.ForeignKey("home.Class_list",on_delete=models.CASCADE)
    subject = models.ForeignKey("home.Subject",on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, validators=[validate_date])
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('class_name','subject','assessment_type',)

    def __str__(self):
        return str(self.class_name)+' - '+str(self.subject)+' - '+str(self.assessment_type)

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    assessment = models.ForeignKey("assessments.Assessment",on_delete=models.CASCADE)
    student = models.ForeignKey("accounts.Student",on_delete=models.CASCADE)
    marks_gained = models.PositiveIntegerField()
    marks_assigned = models.PositiveIntegerField()
    grade = models.CharField(max_length=5, null = True, blank = True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('assessment','student',)