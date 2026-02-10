from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment
from users.models import User

class BookAppointmentView(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['doctor', 'date', 'time_slot', 'symptoms']
    template_name = 'appointments/book_appointment.html'
    success_url = '/dashboard/patient/'

    def form_valid(self, form):
        form.instance.patient = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filter doctors only
        form.fields['doctor'].queryset = User.objects.filter(is_doctor=True)
        return form
