from django.shortcuts import render
from myapp.forms import UserForm, StudentForm


def student_login(request):

    return render(request, "login.html")
