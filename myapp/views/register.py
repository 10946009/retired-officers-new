from django.shortcuts import render
from myapp.forms import UserForm, StudentForm


def register(request):
    user_form = UserForm()
    student_form = StudentForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)

        print(user_form.is_valid())
        print(user_form.errors)
        print(student_form.is_valid())
        print(student_form.errors)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            print("success")
            return render(request, "login.html")
    else:
        user_form = UserForm()
        student_form = StudentForm()

    content = {"user_form": user_form, "student_form": student_form}
    return render(request, "register.html", content)
