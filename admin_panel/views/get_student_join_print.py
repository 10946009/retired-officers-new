from django.shortcuts import  redirect
from django.http import FileResponse, JsonResponse

import requests
from user.models import  ActivityStudents,User
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required

# 環境變數
JASPER_USER=os.environ.get("JASPER_USER")
JASPER_PASSWORD=os.environ.get("JASPER_PASSWORD")

@permission_required('myapp.view_activity', login_url='/403')
def get_student_join_print(request, activity_id, user_id):
    """
    請求jaspersoft的學生報名表資料，得到PDF
    """
    student = User.objects.get(id=user_id)

    # 檢查用戶是否已經認證，檢查是否有報名這個活動
    activity_student = ActivityStudents.objects.get(
        student=student.student, activity_id=activity_id
    )
    if activity_student is None:
        return JsonResponse({"error": "User is not a student"}, status=400)

    try:
        params = {"user_id": user_id, "activity_id": activity_id}
        response = requests.get(
            "http://140.131.116.201:8080/jasperserver/rest_v2/reports/reports/RetiredOfficers/RetiredOfficersJoin.pdf",
            params=params,
            auth=(JASPER_USER, JASPER_PASSWORD),
        )

        if response:
            return FileResponse(
                response, content_type="application/pdf", filename="report.pdf"
            )
        else:
            return JsonResponse("no pdf return", status=400)
    except:
        return JsonResponse("return pdf wrong", status=400)