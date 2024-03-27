
from user.models import Student
from myapp.forms import UserEditForm, StudentForm
from django.contrib.auth.decorators import permission_required
from django.urls import reverse
from django.shortcuts import render

@permission_required('myapp.view_activity', login_url='/403')
def student_update(request,activity_id,student_id):
    print(request.POST)
    if request.user.is_authenticated:
        # 定義表單
        student = Student.objects.get(id=student_id)
        user_form = UserEditForm(instance=student.user)
        student_form = StudentForm(instance=student)
        if request.method == "POST":
            user_form = UserEditForm(request.POST, instance=student.user)
            student_form = StudentForm(request.POST, request.FILES, instance=student)

            if user_form.is_valid() and student_form.is_valid():
                user = user_form.save()
                student = student_form.save(commit=False)
                student.user = user
                student.save()
                return render(request, "message.html", {"next": reverse('student_list', kwargs={'activity_id': activity_id}), "message": "修改成功"})
    content = {"user_form": user_form, "student_form": student_form,'student_id':student_id, 'student':student, 'activity_id':activity_id}
    return render(request, "student_update.html", content)
