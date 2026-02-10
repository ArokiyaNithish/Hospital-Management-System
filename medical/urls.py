from django.urls import path
from . import views

urlpatterns = [
    path('report/upload/', views.UploadReportView.as_view(), name='upload_report'),
    path('daily/create/', views.CreateDailyReportView.as_view(), name='create_daily_report'),
]
