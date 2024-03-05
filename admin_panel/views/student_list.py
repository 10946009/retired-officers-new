from django.shortcuts import render
from myapp.models import Activity
import xlwt
from django.http import HttpResponse

# import custom User model
from user.models import User


def student_list(request, activity_id):
    # get all student of the activity
    activity = Activity.objects.get(id=activity_id)
    students = activity.student_set.all()

    return render(request, "student_list.html", {"students": students})


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
