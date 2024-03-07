from django.shortcuts import render
from myapp.forms import LoginForm

def student_login(request):
    login_form = LoginForm()
    content = {"login_form": login_form}
    
    return render(request, "login.html",content)