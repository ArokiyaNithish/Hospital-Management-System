from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DoctorProfile, PatientProfile

class DoctorProfileInline(admin.StackedInline):
    model = DoctorProfile
    can_delete = False
    verbose_name_plural = 'Doctor Profile'

class PatientProfileInline(admin.StackedInline):
    model = PatientProfile
    can_delete = False
    verbose_name_plural = 'Patient Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (DoctorProfileInline, PatientProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_doctor', 'is_patient')
    list_filter = ('is_staff', 'is_superuser', 'is_doctor', 'is_patient', 'groups')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_doctor', 'is_patient')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
