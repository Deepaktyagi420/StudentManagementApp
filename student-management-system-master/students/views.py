from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Student
from .forms import StudentForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')   # Redirect to index if the user is already logged in
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')   # Redirect to index after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'students/login.html')

def user_logout(request):
    logout(request)
    return redirect('students/login.html')  # Replace 'login' with the name of your login URL


@login_required
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

@login_required
def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))

@login_required
def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })

@login_required
def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })

@login_required
def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))


