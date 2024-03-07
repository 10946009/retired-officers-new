from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
from myapp.forms import LoginForm

def student_login(request):
    message = None
    print('request.user',request.user)
    if request.user.is_authenticated:
        return redirect("/")
    # 如果該email尚未被註冊

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        elif user is None:
            message = "該信箱尚未註冊"
        else:
            message = "帳號或密碼錯誤"
    login_form = LoginForm()
    content = {"login_form": login_form, "message": message}
    
    return render(request, "login.html",content)