from django.shortcuts import redirect,render
from user.models import ActivityStudents
from django.contrib.auth.decorators import permission_required

@permission_required("myapp.view_activity", login_url="/403")
def student_delete(request, activity_id, student_id):
    """
    刪除學生報名資料
    """
    student = ActivityStudents.objects.get(activity_id=activity_id, student_id=student_id)
    # get student
    if request.method == "POST":
        student.delete()
        
    return redirect("student_list", activity_id=activity_id)