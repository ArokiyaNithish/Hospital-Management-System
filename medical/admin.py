from django.contrib import admin
from .models import MedicalReport, Prescription, DailyReport

@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'patient', 'doctor', 'created_at')
    search_fields = ('title', 'patient__username')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'patient', 'doctor', 'prescribed_at')
    search_fields = ('medicine_name', 'patient__username')

@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'mood', 'rating')
    list_filter = ('date', 'rating')
