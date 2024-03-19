from django.shortcuts import render,redirect
from myapp.models import Activity
from django.http import HttpResponse
from openpyxl import Workbook


# import custom User model
from user.models import ActivityStudents


def student_list(request, activity_id):
    '''
    顯示報名學生列表
    '''
    # get all student of the activity
    activity = Activity.objects.get(id=activity_id)
    students = activity.student.all()

    return render(request, "student_list.html", {"students": students, "activity_id": activity_id})

def student_delete(request, student_id):

    return redirect("student_list")

def export_excel(request,activity_id):
    '''
    將報名資料匯出成Excel
    '''
    # 創建一個 Excel 工作簿和工作表
    wb = Workbook()
    ws = wb.active
    ws.title = "MySheet"

    # 將所需的標題資料寫入工作表
    title_list = [
        "編號",
        "姓名",
        "報名編號",
        "虛擬帳號",
        "報名系所",
        "審核",
        "繳費",
        "報名時間",
        "性別",
        "身分證號",
        "生日",
        "住家電話",
        "行動電話",
        "緊急連絡人",
        "連絡人行動電話",
        "與考生關係",
        "電子郵件",
        "郵地區號",
        "通訊地址",
        "畢業學校：",
        "部別",
        "畢肄業",
        "年制",
        "同等學力",
        "畢業系所組",
        "畢(肄)業 年 月",
        "備註",
        "年資",
        "兵籍號碼",
        "軍種",
        "階級",
        "退伍日期",
        "服役年資",
        "一類",
        "二類",
        "備註",
    ]
    ws.append(title_list) # 將標題資料寫入工作表

    # 將學生資料寫入工作表
    students = Activity.objects.get(id=activity_id).student.all() # 取得報名學生資料
    # get student join_time
    for student in students: 
        military_type1 = "一類" if student.military_type == 1 else ""
        military_type2 = "二類" if student.military_type == 2 else ""
        print(student.get_join_time(activity_id))
        student_list = [
            student.id,  # "編號",
            student.user.username,  # "姓名",
            "",  # "報名編號",
            "",  # "虛擬帳號",
            "國軍退除役官兵就讀大學暨技術校院",  # "報名系所",
            "待審",  # "審核",
            "免費",  # "繳費",
            student.get_join_time(activity_id),  # "報名時間",
            student.get_gender_display(),  # "性別",
            student.identity,  # "身分證號",
            student.get_birth_tw(),  # "生日",
            student.home_phone,  # "住家電話",
            student.mobile_phone,  # "行動電話",
            student.emergency_contact,  # "緊急連絡人",
            student.emergency_contact_phone,  # "緊急連絡人行動電話",
            student.emergency_contact_relationship,  # "與考生關係",
            student.get_email(),  # "電子郵件",
            student.postal_code,  # "郵地區號",
            student.address,  # "通訊地址",
            student.graduated_school.name,  # "畢業學校：",
            student.get_graduated_department_display(),  # "部別",
            student.get_is_graduated_display(),  # "畢肄業",
            student.get_graduated_year_display(),  # "年制",
            student.get_education_display(),  # "同等學力",
            student.school_department,  # "畢業系所組",
            student.get_graduated_year_month_tw(),  # "畢(肄)業 年 月",
            student.school_notes,  # "備註",
            student.get_military_service_years_display(),  # "年資",
            student.military_service_number,  # "兵籍號碼",
            student.military_service,  # "軍種",
            student.military_rank,  # "階級",
            student.military_retired_date,  # "退伍日期",
            student.military_service_years_int,  # "服役年資",
            military_type1,  # "一類",
            military_type2,  # "二類",
            student.notes,  # "備註",
        ]
        ws.append(student_list)

    # 將工作簿保存到響應中
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=import_sample.xlsx"
    wb.save(response)

    return response
