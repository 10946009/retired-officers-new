from django.urls import path
from admin_panel.views.activity_list import activity_list
from admin_panel.views.activity_tool_menu import activity_tool_menu
from admin_panel.views.activity_create import activity_create
from admin_panel.views.activity_update import activity_update
from admin_panel.views.activity_delete import activity_delete
from admin_panel.views.student_check_list import student_check_list
from admin_panel.views.student_activity_list import student_activity_list
from admin_panel.views.student_list import student_list, export_excel,student_delete
from admin_panel.views.redirect_user import redirect_user
from admin_panel.views.score_list import (
    score_list,
    export_score_sample,
    upload_and_read_excel,
)

urlpatterns = [
    # activity
    path("activity_list/", activity_list, name="activity_list"),
    path("activity_create/", activity_create, name="activity_create"),
    #活動功能選單
    path("activity_tool_menu/<int:activity_id>", activity_tool_menu, name="activity_tool_menu"),
    #活動功能
    path("activity_tool_menu/activity_update/<int:activity_id>", activity_update, name="activity_update"),
    path("activity_tool_menu/student_check_list/<int:activity_id>", student_check_list, name="student_check_list"), 
    path("activity_tool_menu/activity_delete/<int:activity_id>", activity_delete, name="activity_delete"),
    path("activity_tool_menu/score_list/<int:activity_id>", score_list, name="score_list"),
    # student
    path("student_activity_list/", student_activity_list, name="student_activity_list"),
    path("student_list/<int:activity_id>", student_list, name="student_list"),
    path("student_update/<int:student_id>", student_list, name="student_update"),
    path("student_delete<int:student_id>", student_delete, name="student_delete"),
    path("export_excel/<int:activity_id>", export_excel, name="export_excel"),
    # score
    path("score_activity_list/", student_activity_list, name="score_activity_list"),
    path(
        "export_score_sample/<int:activity_id>",
        export_score_sample,
        name="export_score_sample",
    ),
    path(
        "upload_and_read_excel/<int:activity_id>",
        upload_and_read_excel,
        name="upload_and_read_excel",
    ),
    # check student data

    path("redirect_user/", redirect_user, name="redirect_user"),
]
