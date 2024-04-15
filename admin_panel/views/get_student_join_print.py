from myapp.views.api_data import get_student_join_print_PDF,get_student_score_print_PDF
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_activity', login_url='/403')
def get_student_join_print(request,activity_id, user_id):
    return get_student_join_print_PDF(activity_id, user_id)

@permission_required('myapp.view_activity', login_url='/403')
def get_student_score_print(request,activity_id, user_id):
    return get_student_score_print_PDF(activity_id, user_id)