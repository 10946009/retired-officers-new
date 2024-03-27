from django.shortcuts import render
from myapp.models import Activity
# import custom User model
from django.contrib.auth.decorators import permission_required


@permission_required("myapp.view_activity", login_url="/403")
def student_list(request, activity_id):
    """
    顯示報名學生列表
    """
    # get all student of the activity
    activity = Activity.objects.get(id=activity_id)
    students = activity.student.all()
    content = {"students": students, "activity_id": activity_id}

    return render(request, "student_list.html", content)


