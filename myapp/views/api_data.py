from django.http import  FileResponse, JsonResponse
import requests
from myapp.models import Activity,Score
from user.models import ActivityStudents, User
import os
from django.http import JsonResponse

# 環境變數
JASPER_USER=os.environ.get("JASPER_USER")
JASPER_PASSWORD=os.environ.get("JASPER_PASSWORD")
HEADER_TOKEN = os.environ.get("HEADER_TOKEN")
TEST_ID = 0 
# return JSON
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
    
    if user_id == TEST_ID and activity_id == TEST_ID:
        data = {
            'activity_year' : "110年",
            "number" : "110000",
            "name" : "測試用戶",
            "label_1" : "label1",
            "score1" : "10",
            "label_2" : "label2",
            "score2" : "40",
            "label_3" : "label3",
            "score3" : "50",
            "score_total" : "100",
            "rank": "1",
            "score_min" : "85.55",
        }
        return JsonResponse(data)
    # user宣告 
    user = User.objects.get(id=user_id).student
    
    # models 成績&活動
    score = Score.objects.get(student=user,activity=activity_id)
    activity = Activity.objects.get(id=activity_id)
    rank = activity.get_activity_student_score_rank(user.id)
    if rank is None:
        return JsonResponse({"error": "沒有成績!"}, status=400)

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

# return JSON
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
    
    
    if user_id == TEST_ID and activity_id == TEST_ID:
        data = {
            "activity_year": "113年",
            "number": "1000",
            "year": "65",
            "month": "10",
            "day": "10",
            "name": "測試用戶",
            "idnumber": "A123456789",
            "address": "台北市中正區",
            "home_phone": "0222222222",
            "mobile_phone": "0912345678",
            "email": "study_test@gmail.com",
            "emergency_contact": "測試人",
            "emergency_contact_relationship": "母",
            "emergency_contact_phone": "0912345678",
            "education": "國立中山大學  資訊工程學系",
            "same_education": "是",
            "education_year_month": "65年10月",
            "military_service_number": "A123456789",
            "military_service": "陸軍",
            "military_rank": "上士",
            "military_retired_year": "65",
            "military_retired_month": "10",
            "military_retired_day": "10",
            "military_service_years_int": "10",
            "military_service_years": "10年",
            "identity_front": None, 
            "identity_back": None,
        }
    user = user.student
    try:
        # 身分證正反面宣告(避免有人沒上傳圖片)
        identity_front = None if user.identity_front == "" else user.identity_front.url
        identity_back = None if user.identity_back == "" else user.identity_back.url
        education = f"{user.graduated_school.name}  {user.school_department}"
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
            "same_education": user.get_education_display(),
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


# return PDF
def get_student_join_print_PDF(activity_id, user_id):
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
    
# return PDF
def get_student_score_print_PDF(activity_id, user_id):
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

    # 檢查用戶有沒有成績
    rank = activity_student.activity.get_activity_student_score_rank(student.student.id)
    if rank is None:
        return JsonResponse({"error": "no rank!"}, status=400)
    score = Score.objects.get(student=student.student, activity_id=activity_id)
    if score is None:
        return JsonResponse({"error": "no score!"}, status=400)
     
    try:
        params = {"user_id": user_id, "activity_id": activity_id}
        response = requests.get(
            "http://140.131.116.201:8080/jasperserver/rest_v2/reports/reports/RetiredOfficers/RetiredOfficersScore.pdf",
            params=params,
            auth=(JASPER_USER, JASPER_PASSWORD),
        )

        if response:
            return FileResponse(
                response, content_type="application/pdf", filename="report.pdf"
            )
        else:
            return JsonResponse({"error":"no pdf return"}, status=400)
    except:
        return JsonResponse({"error":"return pdf wrong"}, status=400)