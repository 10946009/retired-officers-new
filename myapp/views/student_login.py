from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
from myapp.forms import LoginForm
from django.contrib.auth import get_user_model
from django.urls import reverse


def student_login(request):
    message = ""
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        print(request.POST)
        print(login_form.is_valid())
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get("password")
            captcha_response = request.POST.get('captcha_1')
            captcha_key = request.POST.get('captcha_0')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("redirect_user")
            else:
                message = "帳號或密碼錯誤"
        else:
            message = "驗證失敗"
    else:
        login_form = LoginForm()
    
    content = {"login_form": login_form, "message": message}
    return render(request, "login.html", content)