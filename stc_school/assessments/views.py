from django.shortcuts import render,redirect,reverse
from django.views.generic import ListView
from assessments.filters import AssessmentTypeFilter
from assessments.forms import AssessmentCreationForm, AssessmentTypeCreationForm
from assessments.models import Assessment, Assessment_type, Result
from home.models import Class_list, Session_year, Subject, Teacher_allocation
from accounts.models import CustomUser, Student, Teacher
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from home.views import Dashboard

# Assessments Types
class AssessmentTypes(ListView):
    model = Assessment_type
    template_name = 'assessments/assessment_type.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assessment_type'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        session = Session_year.objects.last()
        assessment_type = Assessment_type.objects.filter(session_year=session)
        return assessment_type

# Old year assessments types


class OldAssessmentTypes(ListView):
    model = Assessment_type
    template_name = 'assessments/oldAssessments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AssessmentTypeFilter(
            self.request.GET, queryset=self.get_queryset())
        return context

# assessments


class Assessments(ListView):
    model = Assessment
    template_name = 'assessments/assessments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assessment_type = Assessment_type.objects.get(id=self.kwargs['pk'])
        context['assessment'] = Assessment.objects.filter(
            assessment_type=assessment_type)
        context['assessmentType'] = assessment_type
        return context

# results


class Results(ListView):
    model = Class_list
    template_name = "assessments/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = Session_year.objects.last()
        context['sessionName'] = session.sessionYear
        context['classes'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        studentCount = []
        session = Session_year.objects.last()
        sessionClasses = Class_list.objects.filter(session_year=session)
        # sessionClasses = Class_list.objects.filter(
        #     session_year=session, class_teacher=Teacher.objects.get(user_id=self.request.user))
        for each in sessionClasses:
            studentCount.append(Student.objects.filter(
                current_class=each.id).count())
        classes = list(zip(sessionClasses, studentCount))
        return classes



# subject-wise-results
class ClassResults(ListView):
    model = Assessment_type
    template_name = "assessments/resultAssessments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cls = Class_list.objects.get(id=self.kwargs['pk'])
        session = Session_year.objects.get(sessionYear=cls.session_year)
        context['assessments'] = Assessment_type.objects.filter(
            session_year=session)
        context['class'] = cls.id
        context['className'] = cls.class_name + cls.class_section
        return context


class SubjectResults(ListView):
    model = Assessment
    template_name = "assessments/resultSubjects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cls = Class_list.objects.get(id=self.kwargs['pk2'])
        assessment_type = Assessment_type.objects.get(id=self.kwargs['pk1'])
        context['assessments'] = Assessment.objects.filter(
            assessment_type=assessment_type, class_name=cls)
        context['className'] = cls.class_name + cls.class_section
        return context


class StudentResults(ListView):
    model = Result
    template_name = "assessments/resultStudents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Result.objects.filter(
            assessment=self.kwargs['pk'])
        return context


class MyAssessments(ListView):
    model = Assessment
    template_name = 'assessments/myAssessments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assessment = []
        assessment_types = Assessment_type.objects.get(id=self.kwargs['pk'])
        teacher = Teacher.objects.get(user_id=self.request.user)
        session_year = Session_year.objects.last()
        sessionClasses = Teacher_allocation.objects.filter(
            session_year=session_year, teacher=teacher)
        for each in sessionClasses:
            assessment.append(Assessment.objects.get(
                assessment_type=assessment_types, class_name=each.class_name, subject=each.subject))
        context['assessment'] = assessment
        context['assessmentType'] = assessment_types
        return context


class UpdateMarks(ListView):
    model = Student
    template_name = 'assessments/updateMarksStudents.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assessment_types = Assessment_type.objects.get(id=self.kwargs['pk4'])
        className = Class_list.objects.get(id=self.kwargs['pk1'])
        subject = Subject.objects.get(id=self.kwargs['pk2'])
        context['className'] = className
        context['subject'] = subject
        marks = []
        students = Student.objects.filter(current_class=self.kwargs['pk1'])
        for each in students:
            marks.append(Result.objects.get(assessment = self.kwargs['pk3'],student = each))
        context['students'] = zip(students,marks)
        context['assessment'] = self.kwargs['pk3']
        return context


def submitMarks(request,pk):
    if request.method == 'POST':
        print(pk)
        assessment = Assessment.objects.get(id = pk)
        marks = request.POST.getlist('marks')
        grades = request.POST.getlist('grade')
        student = request.POST.getlist('student')
        group = zip(marks,grades,student)
        for a,b,c in group:
            user = CustomUser.objects.get(username=c)
            stud = Student.objects.get(user_id = user)
            Result.objects.filter(assessment = assessment, student = stud).update(marks_gained = a, grade = b)
    return redirect('dashboard')


class CreateAssessment(CreateView):
    model = Assessment
    template_name = "createForms/assessment.html"
    form_class = AssessmentCreationForm
    success_url = reverse_lazy('index')

class UpdateAssessment(UpdateView):
    model = Assessment
    template_name = "createForms/assessment.html"
    form_class = AssessmentCreationForm

    def get_success_url(self):
        return reverse('assessments', kwargs = {'pk': self.kwargs['pk1']})

class DeleteAssessment(DeleteView):
    model = Assessment
    success_url = reverse_lazy('dashboard')


class CreateAssessmentType(CreateView):
    model = Assessment_type
    template_name = "createForms/assessmentType.html"
    form_class = AssessmentTypeCreationForm
    success_url = reverse_lazy('assessmentTypes')

class UpdateAssessmentType(UpdateView):
    model = Assessment_type
    template_name = "createForms/assessmentType.html"
    form_class = AssessmentTypeCreationForm
    success_url = reverse_lazy('assessmentTypes')

    # def get_success_url(self):
    #     return reverse('assessments', kwargs = {'pk': self.kwargs['pk1']})

class DeleteAssessmentType(DeleteView):
    model = Assessment_type
    success_url = reverse_lazy('assessmentTypes')