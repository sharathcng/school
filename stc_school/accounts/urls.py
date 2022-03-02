from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('teachers', views.Teachers.as_view(), name="teachers"),
    path('oldTeachers', views.OldTeacherList.as_view(), name="oldTeachers"),
    path('students/<str:pk1>', views.Students.as_view(), name="students"),
    path('staffs', views.Staffs.as_view(), name="staffs"),
    path('oldStaffs', views.OldStaffList.as_view(), name="oldStaffs"),

    path('studentProfileView/<str:pk>', views.StudentProfileView.as_view(), name="studentProfileView"),
    path('studentProfile/<str:pk>/edit', views.StudentProfileEdit.as_view(), name="studentProfileEdit"),
    path('teacherProfile/<str:pk>', views.TeacherProfileView.as_view(), name="teacherProfileView"),
    path('teacherProfile/<str:pk>/edit', views.TeacherProfileEdit.as_view(), name="teacherProfileEdit"),
    path('staffProfile/<str:pk>', views.StaffProfileView.as_view(), name="staffProfileView"),
    path('staffProfile/<str:pk>/edit', views.StaffProfileEdit.as_view(), name="staffProfileEdit"),

    path('teacher-signup', views.TeacherSignUp.as_view(), name='teacher-signup'),
    path('student-signup', views.StudentSignUp.as_view(), name='student-signup'),
    path('staff-signup', views.StaffSignUp.as_view(), name='staff-signup'),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),

    path('disable-teacher/<str:pk>', views.DisableTeacher.as_view(), name="disable-teacher"),
    path('enable-teacher/<str:pk>', views.EnableTeacher.as_view(), name="enable-teacher"),
    path('disable-old-teacher/<str:pk>', views.DisableOldTeacher.as_view(), name="disable-old-teacher"),
    path('enable-old-teacher/<str:pk>', views.EnableOldTeacher.as_view(), name="enable-old-teacher"),

    path('disable-staff/<str:pk>', views.DisableStaff.as_view(), name="disable-staff"),
    path('enable-staff/<str:pk>', views.EnableStaff.as_view(), name="enable-staff"),
    path('disable-old-staff/<str:pk>', views.DisableOldStaff.as_view(), name="disable-old-staff"),
    path('enable-old-staff/<str:pk>', views.EnableOldStaff.as_view(), name="enable-old-staff"),

    path('disable-student/<str:pk>/<str:pk1>', views.DisableStudent.as_view(), name="disable-student"),
    path('enable-student/<str:pk>/<str:pk1>', views.EnableStudent.as_view(), name="enable-student"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
