from django.shortcuts import redirect, render
from myapp.models import Activity
import openpyxl
from django.http import HttpResponse
from admin_panel.forms import UploadExcelForm
from openpyxl import Workbook

# import custom User model
from user.models import User


def score_list(request, activity_id):

    activity = (
        Activity.objects.select_related("score_label")
        .prefetch_related("student")
        .get(id=activity_id)
    )

    score_label = activity.score_label
    students = activity.student.all()

    # get all students with their scores
    students = [
        {
            "id": student.id,
            "name": student.user.username,
            "email": student.user.email,
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

    return render(
        request,
        "score_list.html",
        {"students": students, "score_label": score_label, "activity": activity},
    )


def export_score_sample(request):
    # 創建一個 Excel 工作簿和工作表
    wb = Workbook()
    ws = wb.active
    ws.title = "MySheet"

    # 向工作表添加一些數據
    # Rest of the code...

    ws.append(["Name", "Age", "City"])
    ws.append(["Alice", 30, "New York"])
    ws.append(["Bob", 25, "Los Angeles"])
    ws.append(["Charlie", 35, "Chicago"])

    # 將工作簿保存到響應中
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=data.xlsx"
    wb.save(response)

    return response


def upload_and_read_excel(request, activity_id):
    print(request.method)
    if request.method == "POST":
        form = UploadExcelForm(request.POST, request.FILES)

        if form.is_valid():
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            ws = wb.active
            data = []
            for row in ws.iter_rows(values_only=True):
                data.append(row)

            print("*" * 50)
            print(data)

            # refresh the page

    # refresh the page
    return redirect("score_list", activity_id=activity_id)
