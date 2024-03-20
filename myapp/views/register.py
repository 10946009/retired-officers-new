from django.shortcuts import render,redirect
from myapp.forms import UserForm, StudentForm


def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)

        print(user_form.is_valid())
        print(user_form.errors)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print("success")
            return redirect('/student_login')
    else:
        user_form = UserForm()

    content = {"user_form": user_form}
    return render(request, "register.html", content)
