from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('', TemplateView.as_view(template_name='home/index.html', extra_context={'title':'STCS - Home Page'})),
    path('', views.Index.as_view(), name="index"),
    path('dashboard', views.Dashboard.as_view(), name="dashboard"),
    path('batches',views.Batches.as_view(), name="batches"),
    path('classes', views.Classes.as_view(), name="classes"),
    path('batchClasses/<str:pk>',views.BatchClasses.as_view(), name="batchClasses"),
    path('edit-class-details/<int:pk>', views.UpdateClassDetails.as_view(), name="edit-class-details"),

    path('myClasses', views.MyClasses.as_view(), name="myClasses"),
    path('create-batch', views.CreateBatch.as_view(), name="create-batch"),
    path('create-class', views.CreateClass.as_view(), name="create-class"),

    path('subjects', views.Subjects.as_view(), name="subjects"),
    path('create-subject', views.CreateSubject.as_view(), name="create-subject"),
    path('edit-subject/<int:pk>', views.EditSubjects.as_view(), name="edit-subject"),

    path('teacher-allocation', views.TeacherAllocation.as_view(), name="teacher-allocation"),
    path('teacher-allocation-create', views.CreateTeacherAllocation.as_view(), name="teacher-allocation-create"),
    path('teacher-allocation-<int:pk>-update', views.UpdateTeacherAllocation.as_view(), name="teacher-allocation-update"),
]
