from django.urls import path

from apps.reports.views import PatientReportCSVView

app_name = 'reports'

urlpatterns = [
    path('patients/csv/', PatientReportCSVView.as_view(), name='patients_csv'),
]
