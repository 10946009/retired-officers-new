from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, JsonResponse
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from myapp.models import Activity
from user.models import User
import os
from myapp.views.print_data import generate_pdf,generate_docx,file_response
from django.contrib.auth import authenticate
from django.http import JsonResponse,HttpResponse
import json
HEADER_TOKEN = os.environ.get('HEADER_TOKEN')
@login_required
def student_print_sign_up(request,activity_id):
    '''
    學生列印報名表
    '''
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
    education = f'{user.graduated_school.name}  {user.school_department} {user.get_education_display()}'
    # data宣告
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



def api_student_print_sign_up(request,user_id,activity_id):
    '''
    學生列印報名表
    '''
    check_auth = request.headers.get('Authorization')
    if check_auth != HEADER_TOKEN:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)
    # if not request.user.is_authenticated:
    #     return redirect("/student_login")

    # 檢查用戶是否已經認證
    # user = authenticate(request)
    # if user is None:
    #     return JsonResponse({'error': 'Invalid credentials'}, status=401)
    
    # models 活動
    try:
        activity = Activity.objects.get(id=activity_id)
    except Activity.DoesNotExist:
        print('Activity does not exist')
        return JsonResponse({'error': 'Activity does not exist'}, status=404)
    # user宣告 & 檔名宣告
    user = User.objects.get(id=user_id)
    if not hasattr(user, 'student'):
        print('User is not a student' )
        return JsonResponse({'error': 'User is not a student'}, status=400)
    user = user.student
    try:
        # 身分證正反面宣告(避免有人沒上傳圖片)
        identity_front = None if user.identity_front == "" else user.identity_front.url
        identity_back = None if user.identity_back == "" else user.identity_back.url
        education = f'{user.graduated_school.name}  {user.school_department} {user.get_education_display()}'
        # data宣告
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
            'education_year_month':user.get_graduated_year_month_tw(),
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
    except Exception as e:
        print(e)
        return JsonResponse({e}, status=500)
    return JsonResponse(data)