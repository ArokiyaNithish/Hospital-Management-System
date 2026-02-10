from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import MedicalReport, DailyReport, Prescription
from users.models import User

class UploadReportView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MedicalReport
    fields = ['patient', 'title', 'file']
    template_name = 'medical/upload_report.html'
    success_url = '/dashboard/doctor/'

    def test_func(self):
        return self.request.user.is_doctor

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filter patients only
        form.fields['patient'].queryset = User.objects.filter(is_patient=True)
        return form

class CreateDailyReportView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DailyReport
    fields = ['mood', 'symptoms_description', 'rating']
    template_name = 'medical/daily_report_form.html'
    success_url = '/dashboard/patient/'

    def test_func(self):
        return self.request.user.is_patient

    def form_valid(self, form):
        form.instance.patient = self.request.user
        return super().form_valid(form)
