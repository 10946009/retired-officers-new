from django.urls import path
from admin_panel.views.activity_list import activity_list
from admin_panel.views.activity_create import activity_create
from admin_panel.views.activity_update import activity_update
from admin_panel.views.activity_delete import activity_delete
from admin_panel.views.student_activity_list import student_activity_list
from admin_panel.views.student_list import student_list, export_excel
from admin_panel.views.score_list import score_list

urlpatterns = [
    # activity
    path("activity_list/", activity_list, name="activity_list"),
    path("activity_create/", activity_create, name="activity_create"),
    path("activity_update/<int:activity_id>", activity_update, name="activity_update"),
    path("activity_delete/<int:activity_id>", activity_delete, name="activity_delete"),
    # student
    path("student_activity_list/", student_activity_list, name="student_activity_list"),
    path("student_list/<int:activity_id>", student_list, name="student_list"),
    path("student_update/<int:student_id>", student_list, name="student_update"),
    path("student_delete<int:student_id>", student_list, name="student_delete"),
    path("export_excel/", export_excel, name="export_excel"),
    # score
    path("score_activity_list/", student_activity_list, name="score_activity_list"),
    path("score_list/<int:activity_id>", score_list, name="score_list"),
]
