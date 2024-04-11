from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from myapp.models import Activity
import os
from myapp.views.print_data import generate_pdf,generate_docx,file_response

@login_required
def student_print_sign_up(request,activity_id):
    if not request.user.is_authenticated:
        return redirect("/student_login")
    if request.user.student is None:
        return redirect("/admin_panel/activity_list/")
    # 範本docx
    sample_name = "sample_sign_up.docx"

    # models 活動
    activity = Activity.objects.get(id=activity_id)
    # docx宣告
    docx_path = os.path.join(os.getcwd(), 'static',sample_name)
    doc = DocxTemplate(docx_path)
    
    # user宣告 & 檔名宣告
    user = request.user.student
    file_name = f"sign_up_{user.id}"
    
    # 身分證正反面宣告(避免有人沒上傳圖片)
    identity_front_text = "【此處請黏貼身分證正面影本】\n未附身分證影本或影本不清晰而無法辨識者，視同報名資格不符，概不予受理。"
    identity_back_text = "【此處請黏貼身分證反面影本】"
    identity_front = identity_front_text if user.identity_front == "" else InlineImage(doc,user.get_identity_front, width=Mm(80))
    identity_back = identity_back_text if user.identity_back == "" else InlineImage(doc,user.get_identity_back, width=Mm(80))
    education = user.graduated_school + user.graduated_department + user.get_education_display()
    data = {
        'activity_year' : activity.get_year_tw(),
        'number':user.activitystudents_set.get(activity_id=activity_id).join_number,
        'year': user.date_of_birth_tw()[0],
        'month':user.date_of_birth_tw()[1],
        'day': user.date_of_birth_tw()[2],
        'name': user.get_username(),
        'idnumber':user.identity,
        'address':user.address,
        'home_phone':user.home_phone,
        'mobile_phone':user.mobile_phone,
        'email':user.get_email(),
        'emergency_contact':user.emergency_contact,
        'emergency_contact_relationship':user.emergency_contact_relationship,
        'emergency_contact_phone':user.emergency_contact_phone,
        'education':education,
        'military_service_number': user.military_service_number,
        'military_service':user.military_service,
        'military_rank':user.military_rank,
        'military_retired_year':user.date_of_military_retired_tw()[0],
        'military_retired_month':user.date_of_military_retired_tw()[1],
        'military_retired_day':user.date_of_military_retired_tw()[2],
        'military_service_years_int':user.military_service_years_int,
        'military_service_years':user.get_military_service_years_display(),
        'identity_front':identity_front,   
        'identity_back':identity_back,
    }

    generate_docx(doc,data,file_name)
    # generate_pdf(f'static/{file_name}.docx', 'static')
    generate_pdf(os.path.join(os.getcwd(), 'static',f'{file_name}.docx'), os.path.join(os.getcwd(), 'static'))
    return file_response(file_name) 