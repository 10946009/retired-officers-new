from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Activity 

@login_required(login_url="/student_login")
def student_join(request, activity_id):
    user = request.user
    print(user.id,activity_id)
    if user.is_authenticated:
        
        if not hasattr(user, 'student'):

            return redirect("/student_edit")
        
        activity = Activity.objects.get(id=activity_id)
        if request.method == "POST":
            user.student.activity.add(activity)
            user.student.join_time = datetime.now()
            user.save()

    return redirect("/")
