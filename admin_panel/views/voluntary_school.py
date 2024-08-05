from django.shortcuts import render
from myapp.models import VoluntarySchool, VoluntaryYear
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render
from myapp.models import Activity, Score
import openpyxl
from django.http import HttpResponse
from admin_panel.forms import UploadExcelForm
from openpyxl import Workbook
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
# import custom User model
from user.models import ActivityStudents
from decimal import Decimal

@permission_required("myapp.view_activity", login_url="/403")
def voluntary_school(request, activity_id):
    voluntary_school = VoluntarySchool.objects.all()
    voluntary_year = VoluntaryYear.objects.all()
    content = {"voluntary_school": voluntary_school, "voluntary_year": voluntary_year, "activity_id": activity_id}
    return render(request, "voluntary_school.html", content)


@permission_required('myapp.view_activity', login_url='/403')
def export_voluntary_sample(request, activity_id):
    '''
    匯入學校志願範本
    '''

    # 創建一個 Excel 工作簿和工作表
    wb = Workbook()
    ws = wb.active
    ws.title = "sample"

    ws.append(
        [
            "校名",
            "學制",
            "類別",
            "系組",
            "核定名額",
            "志願代碼",
        ]
    )
    ws.append(["(請記得刪除範例資料)中國文化大學","在職專班","商管類","國際企業管理學系","2","001"])

    # 將工作簿保存到響應中
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=import_sample.xlsx"
    wb.save(response)

    return response

@permission_required('myapp.view_activity', login_url='/403')
def upload_voluntary_excel(request, activity_id):
    '''
    匯入學校志願
    '''
    
    # refresh the page
    return redirect("score_list", activity_id=activity_id)
