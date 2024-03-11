from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/student_login")
def view_score(request):

    return HttpResponse('view_score')