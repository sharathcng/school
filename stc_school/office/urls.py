from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
        
    path('rdt', RedirectView.as_view(url="https://www.youtube.com"),name='youtube'),
    # path('preload/<str:pk>', views.PreLoadView.as_view(), name="preload"),
    path('attendance-classes', views.AttendanceClasses.as_view(), name="attendance-classes"),
    path('attendance-dates/<int:pk>', views.AttendanceDates.as_view(), name="attendance-dates"),
    path('attendance-students/<str:pk1>/<str:pk2>', views.AttendanceStudents.as_view(), name="attendance-students"),
    path('take-attendance/<str:pk>', views.TakeAttendance.as_view(), name="take-attendance"),
    path('update-old-attendance/<str:pk>', views.UpdateOldAttendance, name = "update-old-attendance"),
    path('save-attendance', views.SaveAttendance.as_view(), name="save-attendance"),
    
]
