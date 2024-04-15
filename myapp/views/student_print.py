from myapp.views.api_data import get_student_join_print_PDF,get_student_score_print_PDF
import os
from django.contrib.auth.decorators import login_required
# 環境變數
JASPER_USER=os.environ.get("JASPER_USER")
JASPER_PASSWORD=os.environ.get("JASPER_PASSWORD")

@login_required
def student_print_sign_up(request, activity_id):
    """
    學生請求jaspersoft的學生報名表資料，得到PDF
    """
    user_id = request.user.id
    
    return get_student_join_print_PDF(activity_id, user_id)

@login_required
def student_print_score(request, activity_id):
    """
    學生請求jaspersoft的學生報名表資料，得到PDF
    """
    user_id = request.user.id
    
    return get_student_score_print_PDF(activity_id, user_id)