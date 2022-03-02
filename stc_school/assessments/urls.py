from django.urls import path
from . import views

urlpatterns = [
    path('assessmentTypes', views.AssessmentTypes.as_view(), name="assessmentTypes"),
    path('oldAssessments', views.OldAssessmentTypes.as_view(), name="oldAssessments"),
    path('assessments/<int:pk>', views.Assessments.as_view(), name="assessments"),
    path('myAssessments/<int:pk>', views.MyAssessments.as_view(), name="myAssessments"),
    path('results', views.Results.as_view(), name="results" ),
    path('class-wise-result/<int:pk>', views.ClassResults.as_view(), name = "class-wise-result"),
    path('subject-wise-result/<int:pk1>/<int:pk2>', views.SubjectResults.as_view(), name = "subject-wise-result"),
    path('student-wise-result/<int:pk>', views.StudentResults.as_view(), name = "student-wise-result"),
    path('update-marks/<int:pk1>/<int:pk2>/<int:pk3>/<int:pk4>', views.UpdateMarks.as_view(), name = "update-marks"),
    path('submitMarks/<int:pk>', views.submitMarks, name="submitMarks"),

    path('create-assessmentType', views.CreateAssessmentType.as_view(), name='create-assessmentType'),
    path('update-assessmentType/<int:pk>/<int:pk1>', views.UpdateAssessmentType.as_view(), name = 'update-assessmentType'),
    path('delete-assessmentType/<int:pk>', views.DeleteAssessmentType.as_view(), name = 'delete-assessmentType'),

    path('create-assessment', views.CreateAssessment.as_view(), name='create-assessment'),
    path('update-assessment/<int:pk>/<int:pk1>', views.UpdateAssessment.as_view(), name = 'update-assessment'),
    path('delete-assessment/<int:pk>', views.DeleteAssessment.as_view(), name = 'delete-assessment'),
]