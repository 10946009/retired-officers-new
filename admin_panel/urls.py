from django.urls import path
from admin_panel.views.activity_list import activity_list
from admin_panel.views.activity_tool_menu import activity_tool_menu
from admin_panel.views.activity_create import activity_create
from admin_panel.views.activity_update import activity_update
from admin_panel.views.activity_delete import activity_delete
from admin_panel.views.student_check_list import student_check_list
from admin_panel.views.student_activity_list import student_activity_list
from admin_panel.views.student_list import student_list
from admin_panel.views.export_excel import export_excel
from admin_panel.views.student_delete import student_delete
from admin_panel.views.student_update import student_update
from admin_panel.views.redirect_user import redirect_user
from admin_panel.views.score_label_list import score_label_list, score_label_delete
from admin_panel.views.score_label_create import score_label_create, score_label_update
from admin_panel.views.get_student_join_print import get_student_join_print
from admin_panel.views.score_list import (
    score_list,
    export_score_sample,
    upload_and_read_excel,
)

urlpatterns = [
    # activity
    path("activity_list/", activity_list, name="activity_list"),
    path("activity_create/", activity_create, name="activity_create"),
    # 活動功能選單
    path(
        "activity_tool_menu/<int:activity_id>",
        activity_tool_menu,
        name="activity_tool_menu",
    ),
    # 活動功能
    path(
        "activity_tool_menu/activity_update/<int:activity_id>",
        activity_update,
        name="activity_update",
    ),
    path(
        "activity_tool_menu/student_check_list/<int:activity_id>",
        student_check_list,
        name="student_check_list",
    ),  # check student data
    path(
        "activity_tool_menu/activity_delete/<int:activity_id>",
        activity_delete,
        name="activity_delete",
    ),
    path(
        "activity_tool_menu/score_list/<int:activity_id>", score_list, name="score_list"
    ),
    # student
    path("student_activity_list/", student_activity_list, name="student_activity_list"),
    path(
        "activity_tool_menu/student_list/<int:activity_id>",
        student_list,
        name="student_list",
    ),
    # get student join by jaspersoft report 
    path(
        "activity_tool_menu/get_student_join_print/<int:user_id>/<int:activity_id>",
        get_student_join_print,
        name="get_student_join_print",
    ),
    path(
        "student_update/<int:activity_id>/<int:student_id>",
        student_update,
        name="student_update",
    ),
    path(
        "student_delete/<int:activity_id>/<int:student_id>",
        student_delete,
        name="student_delete",
    ),
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
    path("score_label_list", score_label_list, name="score_label_list"),
    path("score_label_create", score_label_create, name="score_label_create"),
    path(
        "score_label_delete/<int:score_label_id>",
        score_label_delete,
        name="score_label_delete",
    ),
    path(
        "score_label_update/<int:score_label_id>",
        score_label_update,
        name="score_label_update",
    ),
    # redirect
    path("redirect_user/", redirect_user, name="redirect_user"),
]
