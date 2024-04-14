from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from myapp.models import Activity,Score
import os
from myapp.views.print_data import generate_pdf,generate_docx, file_response

@login_required
def student_print_score(request,activity_id):
    if not request.user.is_authenticated:
        return redirect("/student_login")
    if request.user.student is None:
        return redirect("/admin_panel/activity_list/")
    # 範本docx
    sample_name = "sample_score.docx"
    # models 成績&活動
    score = Score.objects.get(student=request.user.student,activity=activity_id)
    activity = Activity.objects.get(id=activity_id)
    rank = activity.get_activity_student_score_rank(request.user.student.id)
    
    # docx宣告
    docx_path = os.path.join(os.getcwd(), 'static',sample_name)
    doc = DocxTemplate(docx_path)
    
    # user宣告 & 檔名宣告
    user = request.user.student
    file_name = f"score{user.id}"

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
    
    generate_docx(doc,data,file_name)
    generate_pdf(f'static/{file_name}.docx', 'static')
    return file_response(file_name)
