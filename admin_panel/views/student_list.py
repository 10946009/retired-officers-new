from django.shortcuts import render
from myapp.models import Activity
from django.http import HttpResponse
from openpyxl import Workbook


# import custom User model
from user.models import User


def student_list(request, activity_id):
    # get all student of the activity
    activity = Activity.objects.get(id=activity_id)
    students = activity.student.all()

    return render(request, "student_list.html", {"students": students})


def export_excel(request):
    # 創建一個 Excel 工作簿和工作表
    wb = Workbook()
    ws = wb.active
    ws.title = "MySheet"

    # 向工作表添加一些數據
    ws.append(["Name", "Age", "City"])
    ws.append(["Alice", 30, "New York"])
    ws.append(["Bob", 25, "Los Angeles"])
    ws.append(["Charlie", 35, "Chicago"])

    # 將工作簿保存到響應中
    response = HttpResponse(
        content_type="application/msexcel",
    )
    response["Access-Control-Expose-Headers"] = "Content-Disposition"
    # 設置頭部，以便瀏覽器將其作為文件下載
    response["Content-Disposition"] = f'attachment; filename="匯出excel.xlsx"'
    wb.save(response)

    return response
