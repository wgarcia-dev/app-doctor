from django.urls import path
from apps.attention.views.medical_attention import (
    AttentionCreateView,
    AttentionDetailView,
    AttentionListView,
    AttentionUpdateView,
)
from apps.attention.views.appointment import AppointmentCreateView
from apps.attention.views.certificate import CertificateCreateView, CertificateDetailView
 
app_name = 'attention'
urlpatterns = [
  # rutas de atenciones
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  path('appointment_create/', AppointmentCreateView.as_view(), name='appointment_create'),
  path('certificate_create/', CertificateCreateView.as_view(), name='certificate_create'),
  path('certificate/<int:pk>/', CertificateDetailView.as_view(), name='certificate_detail'),
  # path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
]
