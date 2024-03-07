from django.shortcuts import render
from myapp.forms import UserForm, StudentForm


def login(request):
    # content = {"user_form": user_form, "student_form": student_form}
    return render(request, "login.html")
