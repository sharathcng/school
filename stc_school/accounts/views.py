from django.forms import fields
from django.http.response import HttpResponseRedirect
from django.views.generic.base import RedirectView, TemplateView
from accounts.filters import StaffsFilter, TeachersFilter
from accounts.forms import StaffCreationForm, TeacherCreationForm, StudentCreationForm, UpdateStaffForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from accounts.models import CustomUser, Parents_detail, Student, Teacher, Staff
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from home.models import Class_list, Session_year
from accounts.forms import UpdateTeacherForm, UpdateUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.

# Present Teachers


class Teachers(ListView):
    model = Teacher
    template_name = 'accounts/teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        teachers = Teacher.objects.filter(end_date=None)
        return teachers


class Staffs(ListView):
    model = Staff
    template_name = 'accounts/staffs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staffs'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        staffs = Staff.objects.filter(end_date=None)
        return staffs

# Old Teachers


class OldStaffList(ListView):
    model = Staff
    template_name = 'accounts/oldStaffs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StaffsFilter(
            self.request.GET, queryset=self.get_queryset())
        context['staffs'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        teachers = Staff.objects.exclude(end_date=None)
        return teachers


# Old Teachers
class OldTeacherList(ListView):
    model = Teacher
    template_name = 'accounts/oldTeachers.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TeachersFilter(
            self.request.GET, queryset=self.get_queryset())
        context['teachers'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        teachers = Teacher.objects.exclude(end_date=None)
        return teachers

# class students List


class Students(ListView):
    model = Student
    template_name = 'accounts/students.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        className = Class_list.objects.get(id=self.kwargs['pk1'])
        context['className'] = className
        context['students'] = self.get_queryset()
        return context

    def get_queryset(self, *args, **kwargs):
        className = self.kwargs['pk1']
        students = Student.objects.filter(current_class=className)
        return students

# student profile


class StudentProfileView(TemplateView):
    template_name = 'accounts/profileStudent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(username=kwargs['pk'])
        student_id = Student.objects.get(user_id=user_id)
        context['student'] = get_object_or_404(Student, user_id=user_id)
        context['parent'] = get_object_or_404(
            Parents_detail, student_id=student_id)
        return context


class StudentProfileEdit(UpdateView):
    model = Student
    form_class = UpdateUserForm
    template_name = 'editingPages/editStudent.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'studObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        studObj = Student.objects.get(user_id=userObj)
        return studObj


class TeacherProfileView(TemplateView):
    template_name = 'accounts/profileTeacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(username=kwargs['pk'])
        context['teacher'] = get_object_or_404(Teacher, user_id=user_id)
        return context


class TeacherProfileEdit(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    template_name = 'editingPages/editTeacher.html'
    success_url = reverse_lazy('teachers')
    context_object_name = 'teacherObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        teacherObj = Teacher.objects.get(user_id=userObj)
        return teacherObj


class StaffProfileView(TemplateView):
    template_name = 'accounts/profileStaff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = CustomUser.objects.get(username=kwargs['pk'])
        context['staff'] = get_object_or_404(Staff, user_id=user_id)
        return context


class StaffProfileEdit(UpdateView):
    model = Staff
    form_class = UpdateStaffForm
    template_name = 'editingPages/editStaff.html'
    success_url = reverse_lazy('staffs')
    context_object_name = 'staffObj'

    def get_object(self, queryset=None):
        userObj = CustomUser.objects.get(username=self.kwargs['pk'])
        staffObj = Staff.objects.get(user_id=userObj)
        return staffObj


class TeacherSignUp(CreateView):
    model = CustomUser
    template_name = "createForms/teacherRegistration.html"
    form_class = TeacherCreationForm
    initial = {'role': 2}
    success_url = reverse_lazy('teachers')

    def post(self, request, *args, **kwargs):
        fullName = request.POST['full_name']
        date_of_birth = request.POST['dateOfBirth']
        gender = request.POST['gender']
        email_id = request.POST['emaiId']
        phone_number = request.POST['phnNumber'] or None
        blood_group = request.POST['blood']
        aadhaar_number = request.POST['aadhaar'] or None
        present_address = request.POST['presentAddress']
        permanent_address = request.POST['permanentAddress']
        started_date = request.POST['joinDate'] or None
        handling_subjects = request.POST['subjects'] or None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            Teacher.objects.create(user_id=self.object, full_name=fullName, date_of_birth=date_of_birth, gender=gender, email_id=email_id, phone_number=phone_number, blood_group=blood_group,
                                   aadhaar_number=aadhaar_number, handling_subjects= handling_subjects, present_address=present_address, permanent_address=permanent_address, started_date=started_date)
            return self.form_valid(form, **kwargs)

    # def form_valid(self, form):
    #     self.object = form.save()
    #     Teacher.objects.create(user_id=self.object)
    #     return super(TeacherSignUp, self).form_valid(form)


class StudentSignUp(CreateView):
    model = CustomUser
    template_name = "createForms/studentRegistration.html"
    form_class = StudentCreationForm
    initial = {"role": 1}
    success_url = reverse_lazy('classes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classList'] = Class_list.objects.filter(
            session_year=Session_year.objects.last())
        return context

    def post(self, request, *args, **kwargs):
        fullName = request.POST['full_name']
        date_of_birth = request.POST['dateOfBirth']
        place_of_birth = request.POST['placeOfBirth']
        gender = request.POST['gender']
        email_id = request.POST['emaiId']
        phone_number = request.POST['phnNumber'] or None
        blood_group = request.POST['blood']
        aadhaar_number = request.POST['aadhaar'] or None
        present_address = request.POST['presentAddress']
        permanent_address = request.POST['permanentAddress']
        started_class = request.POST['startedClass'] or None
        current_class = Class_list.objects.get(id=request.POST['currentClass'])
        joining_date = request.POST['joinDate'] or None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            newStudent = Student.objects.create(user_id=self.object, full_name=fullName, date_of_birth=date_of_birth, place_of_birth=place_of_birth, gender=gender, email_id=email_id, phone_number=phone_number, blood_group=blood_group,
                                   aadhaar_number=aadhaar_number, present_address=present_address, permanent_address=permanent_address, started_class=started_class, current_class=current_class, joining_date=joining_date)
            messages.success(self.request,"New student created with the name "
            +str(newStudent.full_name)+" for the class "+str(newStudent.current_class)+" ..!!!")
            return self.form_valid(form, **kwargs)

    # def form_valid(self, form):
    #     self.object = form.save()
    #     student = Student.objects.create(user_id=self.object)
    #     Parents_detail.objects.create(student_id=student)
    #     return super().form_valid(form)


class StaffSignUp(CreateView):
    model = CustomUser
    template_name = "createForms/staffRegistration.html"
    form_class = StaffCreationForm
    initial = {"role": 3}
    success_url = reverse_lazy('staffs')

    def post(self, request, *args, **kwargs):
        fullName = request.POST['full_name']
        date_of_birth = request.POST['dateOfBirth']
        gender = request.POST['gender']
        email_id = request.POST['emaiId']
        phone_number = request.POST['phnNumber'] or None
        blood_group = request.POST['blood']
        aadhaar_number = request.POST['aadhaar'] or None
        present_address = request.POST['presentAddress']
        permanent_address = request.POST['permanentAddress']
        started_date = request.POST['joinDate'] or None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.object = form.save()
            Staff.objects.create(user_id=self.object, full_name=fullName, date_of_birth=date_of_birth, gender=gender, email_id=email_id, phone_number=phone_number, blood_group=blood_group,
                                   aadhaar_number=aadhaar_number, present_address=present_address, permanent_address=permanent_address, started_date=started_date)
            return self.form_valid(form, **kwargs)

    # def form_valid(self, form):
    #     self.object = form.save()
    #     return super().form_valid(form)


class Login(LoginView):
    template_name = "loginForms/login.html"

    def get_success_url(self):
        url = self.get_redirect_url()
        if self.request.user.role == 1:
            messages.success(self.request,"Hey, Buddy..! Welcome to STCS dashboard.")
            return reverse_lazy('dashboard')
        elif self.request.user.role == 2:
            messages.success(self.request,"Hi, Buddy..! Welcome to STCS dashboard.")
            return reverse_lazy('dashboard')


class Logout(LogoutView):
    next_page = reverse_lazy('login')


class DisableStudent(RedirectView):
    pattern_name = 'students'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args, kwargs['pk1'])


class EnableStudent(RedirectView):
    pattern_name = 'students'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args, kwargs['pk1'])


class DisableTeacher(RedirectView):
    pattern_name = 'teachers'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args)


class EnableTeacher(RedirectView):
    pattern_name = 'teachers'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args)


class DisableOldTeacher(RedirectView):
    pattern_name = 'oldTeachers'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args)


class EnableOldTeacher(RedirectView):
    pattern_name = 'oldTeachers'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args)


class DisableStaff(RedirectView):
    pattern_name = 'staffs'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args)


class EnableStaff(RedirectView):
    pattern_name = 'staffs'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args)


class DisableOldStaff(RedirectView):
    pattern_name = 'oldStaffs'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(
            username=kwargs['pk']).update(is_active=False)
        return super().get_redirect_url(*args)


class EnableOldStaff(RedirectView):
    pattern_name = 'oldStaffs'

    def get_redirect_url(self, *args, **kwargs):
        CustomUser.objects.filter(username=kwargs['pk']).update(is_active=True)
        return super().get_redirect_url(*args)
