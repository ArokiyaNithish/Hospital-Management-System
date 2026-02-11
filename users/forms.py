from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, DoctorProfile, PatientProfile

class DoctorRegistrationForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    available_days = forms.CharField(max_length=200, help_text="e.g. Mon,Tue,Wed")
    consultation_fee = forms.DecimalField(max_digits=10, decimal_places=2)
    image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            DoctorProfile.objects.create(
                user=user,
                specialization=self.cleaned_data['specialization'],
                bio=self.cleaned_data['bio'],
                available_days=self.cleaned_data['available_days'],
                consultation_fee=self.cleaned_data['consultation_fee'],
                image=self.cleaned_data['image']
            )
        return user

class PatientRegistrationForm(UserCreationForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    blood_group = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user,
                dob=self.cleaned_data['dob'],
                blood_group=self.cleaned_data['blood_group'],
                address=self.cleaned_data['address']
            )
        return user
