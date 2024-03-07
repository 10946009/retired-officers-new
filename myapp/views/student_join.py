from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/student_login")
def student_join(request, activity_id):

    return render(request, "login.html")
