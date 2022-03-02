from django.db import models


#Session Year Model
class Session_year(models.Model):
    sessionYear = models.CharField(max_length=50,primary_key=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sessionYear

class Class_list(models.Model):
    id = models.AutoField(primary_key=True)
    session_year = models.ForeignKey("home.Session_year",on_delete=models.CASCADE)
    class_name = models.CharField(max_length=255)
    class_section = models.CharField(max_length=255)
    class_teacher = models.ForeignKey("accounts.Teacher", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '\''+self.class_name+self.class_section+'\''
    class Meta:
        unique_together = (['session_year','class_name','class_section','class_teacher'])

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject_name
    class Meta:
        unique_together = (['subject_name'])

class Teacher_allocation(models.Model):
    id = models.AutoField(primary_key=True)
    session_year = models.ForeignKey("home.Session_year",on_delete=models.CASCADE)
    class_name = models.ForeignKey("home.Class_list",on_delete=models.CASCADE)
    subject = models.ForeignKey("home.Subject",on_delete=models.CASCADE)
    teacher = models.ForeignKey("accounts.Teacher",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session_year','class_name','subject',)

