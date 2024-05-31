from django.shortcuts import render
from myapp.models import ActivityStudents
# import custom User model
from django.contrib.auth.decorators import permission_required


@permission_required("myapp.view_activity", login_url="/403")
def student_list(request, activity_id):
    """
    顯示報名學生列表
    """
    # get all student of the activity , order by join_time
    students = ActivityStudents.objects.filter(activity_id=activity_id).order_by("join_time")
    content = {"students": students, "activity_id": activity_id}

    return render(request, "student_list.html", content)


