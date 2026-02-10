from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/doctor/', views.DoctorRegisterView.as_view(), name='register_doctor'),
    path('register/patient/', views.PatientRegisterView.as_view(), name='register_patient'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
