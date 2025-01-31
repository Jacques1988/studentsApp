from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentAPISerializer
# Create your views here.

class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentAPISerializer