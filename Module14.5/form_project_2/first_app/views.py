from django.shortcuts import render,redirect
from .import models

# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def show_data(request):
    student = models.StudentModel.objects.all()
    return render(request, 'first_app/show_data.html', {'student': student})

def delete_student(request,roll):
    data = models.StudentModel.objects.get(pk = roll).delete()
    return redirect('show_data')