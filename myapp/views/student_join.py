from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Activity 
#forms
from myapp.forms import UserEditForm, StudentForm

@login_required(login_url="/student_login")
def student_join(request,activity_id):
    if request.user.is_authenticated:
        # 定義表單
        user_form = UserEditForm(instance=request.user)
        # 如果使用者使用Google登入 沒有student的話，就建立一個student
        if hasattr(request.user, 'student'):
            student_form = StudentForm(instance=request.user.student)
        else:
            student_form = StudentForm()

        if request.method == "POST":
            user_form = UserEditForm(request.POST, instance=request.user)
            if hasattr(request.user, 'student'):
                student_form = StudentForm(request.POST, request.FILES, instance=request.user.student)
            else:
                #create a new student
                student_form = StudentForm(request.POST, request.FILES)
            if user_form.is_valid() and student_form.is_valid():
                user = user_form.save()
                student = student_form.save(commit=False)
                student.user = user
                student.save()
                if request.POST.get("saveValue") == "0":
                    activity = Activity.objects.get(id=activity_id)
                    user.student.activity.add(activity)
                    user.student.join_time = datetime.now()
                    user.save()
                    return render(request, "message.html", {"next": "/", "message": "報名成功!至首頁列印報名表"})
                else:
                    return render(request, "message.html", {"next": f"/student_join/{activity_id}", "message": "儲存成功"})
    content = {"user_form": user_form, "student_form": student_form, "activity_id": activity_id}
    return render(request, "student_join.html", content)