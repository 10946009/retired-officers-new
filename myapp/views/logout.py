from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/student_login")
def logout(request):
    # logout the user
    request.session.flush()

    return redirect("/")