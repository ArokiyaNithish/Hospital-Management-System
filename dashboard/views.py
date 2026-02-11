from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from appointments.models import Appointment
from medical.models import MedicalReport, Prescription

class DoctorDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/doctor_dashboard.html'

    def test_func(self):
        return self.request.user.is_doctor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Assuming user is User instance, but we need to query based on filtering
        # The relationships in models are settings.AUTH_USER_MODEL
        doctor = self.request.user
        context['pending_appointments'] = Appointment.objects.filter(doctor=doctor, status='pending')
        context['upcoming_appointments'] = Appointment.objects.filter(doctor=doctor, status='confirmed')
        # We need to filter reports where doctor is assigned or maybe all reports of their patients?
        # For now, reports uploaded by this doctor or assigned to this doctor
        context['recent_reports'] = MedicalReport.objects.filter(doctor=doctor).order_by('-created_at')[:5]
        return context

class PatientDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/patient_dashboard.html'

    def test_func(self):
        return self.request.user.is_patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.request.user
        context['appointments'] = Appointment.objects.filter(patient=patient).order_by('date')
        context['reports'] = MedicalReport.objects.filter(patient=patient).order_by('-created_at')
        context['prescriptions'] = Prescription.objects.filter(patient=patient).order_by('-prescribed_at')
        return context
