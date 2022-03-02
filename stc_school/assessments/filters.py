import django_filters
from assessments.models import Assessment_type

class AssessmentTypeFilter(django_filters.FilterSet):

    class Meta:
        model = Assessment_type
        fields = ['session_year',]