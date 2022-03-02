

# class PreLoadView(RedirectView):
#     pattern_name = 'singleStudent'
#     def get_redirect_url(self, *args, **kwargs):
#         user_id = CustomUser.objects.get(username=kwargs['pk'])
#         user = Student.objects.filter(user_id = user_id)
#         user.update(current_class = '8A')
#         return super().get_redirect_url(*args, **kwargs)

from django.db import transaction
from datetime import datetime, date
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import FormView
from home.models import Class_list, Session_year
from office import models
from office.models import Attendance
from accounts.models import Student
from django.views.generic import ListView, UpdateView


class AttendanceClasses(ListView):
    model = Class_list
    template_name = 'attendance/attendanceClasses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        studentCount = []
        session = Session_year.objects.last()
        sessionClasses = Class_list.objects.filter(session_year=session)
        for each in sessionClasses:
            studentCount.append(Student.objects.filter(
                current_class=each.id).count())
        context['classes'] = list(zip(sessionClasses, studentCount))
        return context


class AttendanceDates(ListView):
    model = Attendance
    template_name = 'attendance/attendanceDates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        className = Class_list.objects.get(id=self.kwargs['pk'])
        attendance = Attendance.objects.filter(class_name=className).values('date').distinct()
        context['attendance'] = attendance
        context['className'] = className
        return context


class AttendanceStudents(ListView):
    model = Attendance
    template_name = 'attendance/attendanceStudents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dates = datetime.strptime(
            self.kwargs['pk2'], '%Y-%m-%d').strftime('%Y-%m-%d')
        className = Class_list.objects.get(id=self.kwargs['pk1'])
        attendance = Attendance.objects.filter(
            class_name=className, date=dates)
        context['attendance'] = attendance
        context['className'] = className
        return context


class TakeAttendance(ListView):
    model = Attendance
    template_name = 'attendance/attendanceStudents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        className = Class_list.objects.get(id=self.kwargs['pk'])
        students = Student.objects.filter(current_class=className)
        with transaction.atomic():
            for stud in students:
                Attendance.objects.update_or_create(class_name=className, date=date.today(), student=stud)
        attendance = Attendance.objects.filter(class_name=className, date=date.today())
        context['attendance'] = attendance
        context['className'] = className
        return context


def UpdateOldAttendance(request, pk):
    if request.method == 'POST':
        className = Class_list.objects.get(id=pk)
        students = Student.objects.filter(current_class=className)
        oldDate = request.POST['oldDate']
        with transaction.atomic():
            for stud in students:
                Attendance.objects.update_or_create(class_name=className, date=oldDate, student=stud)
        attendance = Attendance.objects.filter(
            class_name=className, date=oldDate)
        return render(request, 'attendance/attendanceStudents.html', {'attendance': attendance, 'className': className})


class SaveAttendance(FormView):
    def post(self, request, *args, **kwargs):
        classID = request.POST['className']
        className = Class_list.objects.get(id = classID)
        attendance = Attendance.objects.filter(class_name=className).values('date').distinct()
        className
        sid = request.POST.getlist('sid')
        morning = request.POST.getlist('morning')
        afternoon = request.POST.getlist('afternoon')
        with transaction.atomic():
            for each in sid:
                if each in morning:
                    Attendance.objects.filter(id=each).update(morng_presence=True)
                else:
                    Attendance.objects.filter(id=each).update(morng_presence=False)
                if each in afternoon:
                    Attendance.objects.filter(id=each).update(aftrn_presence=True)
                else:
                    Attendance.objects.filter(id=each).update(aftrn_presence=False)
        return render(request,'attendance/attendanceDates.html', {'className': className, 'attendance':attendance})