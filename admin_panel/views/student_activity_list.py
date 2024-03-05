from django.shortcuts import render
from myapp.models import Activity


def student_activity_list(request):
    # get all activties
    activities = Activity.objects.all()

    # if path is student_activity_list, view_url_name is student_list

    if request.path == "/admin_panel/student_activity_list/":
        view_url_name = "student_list"
        title = "學生資料管理"
    elif request.path == "/admin_panel/score_activity_list/":
        title = "學生成績管理"
        view_url_name = "score_list"

    return render(
        request,
        "student_activity_list.html",
        {"activities": activities, "view_url_name": view_url_name, "title": title},
    )
