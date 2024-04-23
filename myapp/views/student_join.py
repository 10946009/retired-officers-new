from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Activity 
from user.models import ActivityStudents
#forms
from myapp.forms import UserEditForm, StudentForm
from django.urls import reverse
default_number = 1000

@login_required
def student_join(request,activity_id):
    print(request.POST)
    if request.user.is_authenticated:
        # 如果活動不存在，就導回首頁
        if not Activity.objects.filter(id=activity_id).exists():
            print("活動不存在")
            return render(request, "message.html", {"next": reverse("index"), "message": "活動不存在"})
        
        #如果不在活動時間內，就導回首頁
        activity = Activity.objects.get(id=activity_id)
        print("activity.is_sign_up_open",activity.is_sign_up_open())
        if not activity.is_sign_up_open() :
            print("不在報名時間內")
            return render(request, "message.html", {"next": reverse("index"), "message": "不在報名時間內"})

        # 定義表單
        user_form = UserEditForm(instance=request.user)
        # 如果使用者使用Google登入 沒有student的話，就建立一個student
        if hasattr(request.user, 'student'):
            # 如果已經報名過，就導回首頁
            if ActivityStudents.objects.filter(activity_id=activity_id, student_id=request.user.student.id).exists():
                return redirect("/")
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
                    join_number = default_number + ActivityStudents.objects.count() + 1
                    activty_student = ActivityStudents.objects.create(activity=activity, student=student, join_number=join_number,checked_number="")
                    activty_student.save()
                    return render(request, "message.html", {"next": reverse("index"), "message": "報名成功!至首頁列印報名表"})
                else:
                    return render(request, "message.html", {"next": f"/student_join/{activity_id}", "message": "儲存成功"})
    content = {"user_form": user_form, "student_form": student_form, "activity_id": activity_id}
    return render(request, "student_join.html", content)