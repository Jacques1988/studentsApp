from django.urls import path
from .views import StudentAPIView, StudentDetailAPIView


urlpatterns = [
    path('students/', StudentAPIView.as_view(), name="name"),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student_detail')
]