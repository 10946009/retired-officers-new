from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Activity 
#forms
from myapp.forms import UserEditForm, StudentForm

@login_required(login_url="/student_login")
def student_edit(request):
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
                
            print(student_form.errors)
            print(user_form.errors)
            if user_form.is_valid() and student_form.is_valid():
                user = user_form.save()
                student = student_form.save(commit=False)
                student.user = user
                student.save()
                return redirect('/student_login')
    content = {"user_form": user_form, "student_form": student_form}
    return render(request, "student_edit.html", content)