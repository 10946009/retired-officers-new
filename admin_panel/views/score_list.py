from django.shortcuts import render
from myapp.models import Activity
import xlwt
from django.http import HttpResponse

# import custom User model
from user.models import User


def score_list(request, activity_id):
    # get all student of the activity
    activity = Activity.objects.get(id=activity_id)
    # get score_label of the activity
    score_label = activity.score_label
    print(score_label)
    print(score_label)

    students = activity.student.all()

    # get all students with their scores
    students = [
        {
            "id": student.id,
            "name": student.user.username,
            "score1": student.score_set.get(activity=activity).score1,
            "score2": student.score_set.get(activity=activity).score2,
            "score3": student.score_set.get(activity=activity).score3,
            "total": student.score_set.get(activity=activity).score1
            * score_label.score1_weight
            / 100
            + student.score_set.get(activity=activity).score2
            * score_label.score2_weight
            / 100
            + student.score_set.get(activity=activity).score3
            * score_label.score3_weight
            / 100,
        }
        for student in students
    ]

    return render(request, "score_list.html", {"students": students})


def export_excel(request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Users")

    # Sheet header
    ws.write(0, 0, "Username")
    ws.write(0, 1, "Email")

    # Sheet body
    users = User.objects.all()
    row_num = 1
    for user in users:
        ws.write(row_num, 0, user.username)
        ws.write(row_num, 1, user.email)
        row_num += 1

    wb.save(response)
    return response
