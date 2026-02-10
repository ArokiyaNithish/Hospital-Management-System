from django.db import models
from django.conf import settings

class MedicalReport(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='medical_reports')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='uploaded_reports')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Prescription(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='prescribed_medications')
    medicine_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_name

class DailyReport(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='daily_reports')
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=50) # Can be a choice field
    symptoms_description = models.TextField()
    rating = models.IntegerField(help_text="Health rating from 1 to 10")

    def __str__(self):
        return f"Daily Report: {self.patient} - {self.date}"
