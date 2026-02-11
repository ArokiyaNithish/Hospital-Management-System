from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('patient/', views.PatientDashboardView.as_view(), name='patient_dashboard'),
]
