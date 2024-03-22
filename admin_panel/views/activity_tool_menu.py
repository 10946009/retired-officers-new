from django.shortcuts import render
from myapp.models import Activity
from django.contrib.auth.decorators import permission_required


@permission_required("myapp.view_activity", login_url="/403")
def activity_tool_menu(request, activity_id):
    activity = Activity.objects.get(id=activity_id)

    tools = [
        {
            "name": "活動編輯",
            "url": "activity_update",
            "icon": "fas fa-edit",
            "style": "secondary",
        },
        {
            "name": "學生資料",
            "url": "student_list",
            "icon": "fas fa-file-signature",
            "style": "primary",
        },
        {
            "name": "資料審查",
            "url": "student_check_list",
            "icon": "fas fa-file-alt",
            "style": "success",
        },
        {
            "name": "成績管理",
            "url": "score_list",
            "icon": "fas fa-user-plus",
            "style": "info",
        },
    ]

    content = {"activity": activity, "tools": tools}
    return render(request, "activity_tool_menu.html",content)
