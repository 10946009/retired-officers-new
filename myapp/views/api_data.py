from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import  JsonResponse
from myapp.models import Activity,Score
from user.models import User
import os
from myapp.views.print_data import generate_pdf, generate_docx, file_response
from django.contrib.auth import authenticate
from django.http import JsonResponse

HEADER_TOKEN = os.environ.get("HEADER_TOKEN")

def api_student_print_score(request):
    """
    學生列印成績單API，得到學生JSON資料。params: user_id, activity_id
    """

    user_id = request.GET.get("user_id")
    activity_id = request.GET.get("activity_id")
    if user_id is None or activity_id is None:
        return JsonResponse({"error": "Invalid parameters"}, status=400)
    
    # 檢查用戶是否已經認證
    check_auth = request.headers.get("Authorization")
    if check_auth != HEADER_TOKEN:
        return JsonResponse({"error": "TOKEN error"}, status=401)

    # user宣告 
    user = User.objects.get(id=user_id).student
    
    # models 成績&活動
    score = Score.objects.get(student=user,activity=activity_id)
    activity = Activity.objects.get(id=activity_id)
    rank = activity.get_activity_student_score_rank(user.id)
    

    data = {
        'activity_year' : activity.get_year_tw(),
        "number" : user.get_checked_number(activity_id),
        "name" : user.get_username(),
        "label_1" : activity.score_label.label1,
        "score1" : format(score.score1, '.2f'),
        "label_2" : activity.score_label.label2,
        "score2" : format(score.score2, '.2f'),
        "label_3" : activity.score_label.label3,
        "score3" : format(score.score3, '.2f'),
        "score_total" : format(score.get_total_score(), '.2f'),
        "rank": rank,
        "score_min" : activity.score_min,
    }
    return JsonResponse(data)


def api_student_print_sign_up(request):
    """
    學生列印報名表 API，得到學生JSON資料。params: user_id, activity_id
    """
    user_id = request.GET.get("user_id")
    activity_id = request.GET.get("activity_id")
    if user_id is None or activity_id is None:
        return JsonResponse({"error": "Invalid parameters"}, status=400)
    # 檢查用戶是否已經認證
    check_auth = request.headers.get("Authorization")
    if check_auth != HEADER_TOKEN:
        return JsonResponse({"error": "TOKEN error"}, status=401)

    try:
        activity = Activity.objects.get(id=activity_id)
    except Activity.DoesNotExist:
        print("Activity does not exist")
        return JsonResponse({"error": "Activity does not exist"}, status=404)
    # user宣告 & 檔名宣告
    user = User.objects.get(id=user_id)
    if not hasattr(user, "student"):
        print("User is not a student")
        return JsonResponse({"error": "User is not a student"}, status=400)
    user = user.student
    try:
        # 身分證正反面宣告(避免有人沒上傳圖片)
        identity_front = None if user.identity_front == "" else user.identity_front.url
        identity_back = None if user.identity_back == "" else user.identity_back.url
        education = f"{user.graduated_school.name}  {user.school_department} {user.get_education_display()}"
        # data宣告
        data = {
            "activity_year": activity.get_year_tw(),
            "number": user.activitystudents_set.get(
                activity_id=activity_id
            ).join_number,
            "year": user.date_of_birth_tw()[0],
            "month": user.date_of_birth_tw()[1],
            "day": user.date_of_birth_tw()[2],
            "name": user.get_username(),
            "idnumber": user.identity,
            "address": user.address,
            "home_phone": user.home_phone,
            "mobile_phone": user.mobile_phone,
            "email": user.get_email(),
            "emergency_contact": user.emergency_contact,
            "emergency_contact_relationship": user.emergency_contact_relationship,
            "emergency_contact_phone": user.emergency_contact_phone,
            "education": education,
            "education_year_month": user.get_graduated_year_month_tw(),
            "military_service_number": user.military_service_number,
            "military_service": user.military_service,
            "military_rank": user.military_rank,
            "military_retired_year": user.date_of_military_retired_tw()[0],
            "military_retired_month": user.date_of_military_retired_tw()[1],
            "military_retired_day": user.date_of_military_retired_tw()[2],
            "military_service_years_int": user.military_service_years_int,
            "military_service_years": user.get_military_service_years_display(),
            "identity_front": identity_front,
            "identity_back": identity_back,
        }
    except Exception as e:
        print(e)
        return JsonResponse({e}, status=500)
    return JsonResponse(data)
