from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    bio = models.TextField(blank=True)
    available_days = models.CharField(max_length=200, help_text="e.g. Mon,Tue,Wed")
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Dr. {self.user.username}"

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    dob = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
