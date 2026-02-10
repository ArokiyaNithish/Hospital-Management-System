from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import DoctorRegistrationForm, PatientRegistrationForm
from .models import User
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView

def register(request):
    return render(request, 'registration/register_landing.html')

class DoctorRegisterView(CreateView):
    model = User
    form_class = DoctorRegistrationForm
    template_name = 'registration/register_doctor.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # Redirect based on role
        return redirect('doctor_dashboard')

class PatientRegisterView(CreateView):
    model = User
    form_class = PatientRegistrationForm
    template_name = 'registration/register_patient.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient_dashboard')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_doctor:
            return '/dashboard/doctor/'
        elif user.is_patient:
            return '/dashboard/patient/'
        return '/'
