from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('accounts.urls')),
    path('',include('assessments.urls')),
    path('',include('office.urls')),
]
