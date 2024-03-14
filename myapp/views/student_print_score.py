from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from myapp.models import Activity,Score
import os
from myapp.views.print_data import generate_pdf,generate_docx, file_response

@login_required(login_url="/student_login")
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
    # docx宣告
    docx_path = os.path.join(os.getcwd(), 'static',sample_name)
    doc = DocxTemplate(docx_path)

    # user宣告 & 檔名宣告
    user = request.user.student
    file_name = f"score{user.id}"

    score_total = (score.score1*activity.score_label.score1_weight + score.score2*activity.score_label.score2_weight + score.score3*activity.score_label.score3_weight)/100

    data = {
        'activity_year' : activity.get_year_tw(),
        "number" : user.id,
        "name" : user.get_username(),
        "label_1" : activity.score_label.label1,
        "score1" : score.score1,
        "label_2" : activity.score_label.label2,
        "score2" : score.score2,
        "label_3" : activity.score_label.label3,
        "score3" : score.score3,
        "score_total" : score_total
    }

    generate_docx(doc,data,file_name)
    generate_pdf(f'static/{file_name}.docx', 'static')
    return file_response(file_name)
