from django.shortcuts import render, redirect
from .models import Student

def home_view(request):
    return render(request, 'home.html')

def register_student(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST.get('student_id'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            contact_no=request.POST.get('contact_no')
        )
        return redirect('registration')

    return render(request, 'registration.html')