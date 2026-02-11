from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookAppointmentView.as_view(), name='book_appointment'),
]
