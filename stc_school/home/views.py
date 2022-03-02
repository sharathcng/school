from pyexpat import model
from re import template

from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from accounts.models import CustomUser, Student, Teacher
from home import models
from home.forms import BatchCreationForm, ClassCreationForm, SubjectCreationForm, TeacherAllocationCreationForm, TeacherAllocationUpdateForm, UpdateClassForm, UpdateSubjectForm
from home.models import Class_list, Session_year, Subject, Teacher_allocation
from django.contrib import messages

# home page
# def index(request):
#     return render(request,"home/index.html")

#home page
class Index(TemplateView):
    template_name = "home/index.html"

# dashboard page
class Dashboard(TemplateView):
    template_name = 'home/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user.is_authenticated == True:
        #     if self.request.user.role == 1:
        #         uid = Student.objects.get(user_id = self.request.user)
        #         context['current_user'] = uid
        #     elif self.request.user.role == 2:
        #         uid = Teacher.objects.get(user_id = self.request.user)
        #         if self.request.user.is_classTeacher == True:
        #             cls = Class_list.objects.get(session_year = Session_year.objects.last(),class_teacher = uid)
        #             context['class_teacher'] = cls
        #             context['current_user'] = uid
        # else:
        #     None
        return context
    
    # def get_data(self):
    #     students = Student.objects.all()
    #     return students

#Displaying all batches in a list
class Batches(ListView):
    model = Session_year
    template_name = "home/batches.html"
    context_object_name = 'sessions'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        sessions = Session_year.objects.all().order_by('-sessionYear')
        return sessions

#Batchwise classes list        
class BatchClasses(ListView):
    model = Session_year
    template_name = "home/classes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        studentCount = []
        session = Session_year.objects.get(sessionYear = self.kwargs['pk'])
        sessionClasses = Class_list.objects.filter(session_year = session)
        for each in sessionClasses:
            studentCount.append(Student.objects.filter(current_class = each.id).count())
        context['classes'] = list(zip(sessionClasses, studentCount))
        if session:
            context['sessionName'] = session.sessionYear
        else:
            None
        return context

#Present year classes list
class Classes(ListView):
    model = Class_list
    template_name = "home/classes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = Session_year.objects.last()   
        context['classes'] = self.get_queryset()
        if session:
            context['sessionName'] = session.sessionYear
        else:
            None
        return context
    
    def get_queryset(self, *args, **kwargs):
        studentCount = []
        session = Session_year.objects.last()   
        sessionClasses = Class_list.objects.filter(session_year = session)
        for each in sessionClasses:
            studentCount.append(Student.objects.filter(current_class = each.id).count())
        classes = list(zip(sessionClasses, studentCount))
        return classes

class MyClasses(ListView):
    model = Class_list
    template_name = "home/myClasses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = Session_year.objects.last()   
        context['classes'] = self.get_queryset()
        if session:
            context['sessionName'] = session.sessionYear
        else:
            None
        return context
    
    def get_queryset(self, *args, **kwargs):
        studentCount = []
        session = Session_year.objects.last() 
        if self.request.user.role == 2 and self.request.user.is_superuser == False:
            sessionClasses = Teacher_allocation.objects.filter(session_year = session, teacher = Teacher.objects.get(user_id = self.request.user))
            for each in sessionClasses:
                studentCount.append(Student.objects.filter(current_class = each.class_name).count())
            classes = list(zip(sessionClasses, studentCount))
            return classes


class CreateClass(CreateView):
    model = Class_list
    template_name = "createForms/class.html"
    form_class = ClassCreationForm

    def get_success_url(self):
        # messages.success(self.request,"You have created a new class..!!!")
        return reverse_lazy('classes')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request,"You have created a new class with the name "+
        "\""+self.object.class_name+" " +self.object.class_section+"\"..!!!")
        return super().form_valid(form)

class CreateBatch(CreateView):
    model = Session_year
    template_name = "createForms/batch.html"
    form_class = BatchCreationForm
    # success_url = reverse_lazy('batches')
    # success_message =  messages.success(request,"You have created a new batch for this year..!!!")
    def get_success_url(self):
        messages.success(self.request,"You have created a new batch for this year..!!!")
        return reverse_lazy('batches')

class Subjects(ListView):
    model = Subject
    template_name = "office/subjects.html"

class CreateSubject(CreateView):
    model = Subject
    template_name = "createForms/subject.html"
    form_class = SubjectCreationForm
    success_url = reverse_lazy('subjects')

class EditSubjects(UpdateView):
    model = Subject
    form_class = UpdateSubjectForm
    template_name = 'editingPages/editSubject.html'
    success_url = reverse_lazy('subjects')
    context_object_name = 'subjectObj'

    def get_object(self, queryset=None):
        subjectObj = Subject.objects.get(id=self.kwargs['pk'])
        return subjectObj

class UpdateClassDetails(UpdateView):
    model = Class_list
    template_name = 'editingPages/editClass.html'
    form_class = UpdateClassForm
    success_url = reverse_lazy('classes')
    context_object_name = 'subjectObj'

    def get_object(self, queryset=None):
        subjectObj = Class_list.objects.get(id=self.kwargs['pk'])
        return subjectObj


class CreateTeacherAllocation(CreateView):
    model = Teacher_allocation
    template_name = "createForms/teacherAllocation.html"
    form_class = TeacherAllocationCreationForm
    success_url = reverse_lazy('teacher-allocation')

class TeacherAllocation(ListView):
    model = Teacher_allocation
    template_name = "home/teacherAllocations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = Session_year.objects.last()   
        context['teacherAllocation'] = Teacher_allocation.objects.filter(session_year = Session_year.objects.last())
        if session:
            context['sessionName'] = session.sessionYear
        else:
            None
        return context
        
class UpdateTeacherAllocation(UpdateView):
    model = Teacher_allocation
    form_class = TeacherAllocationUpdateForm
    template_name = 'editingPages/editTeacherAllocation.html'
    success_url = reverse_lazy('teacher-allocation')
    context_object_name = 'teacherAllocation'

    def get_object(self, queryset=None):
        teacherAllocation = Teacher_allocation.objects.get(id=self.kwargs['pk'])
        return teacherAllocation