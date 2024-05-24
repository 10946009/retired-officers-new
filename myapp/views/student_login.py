from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
from myapp.forms import LoginForm
from django.contrib.auth import get_user_model
from django.urls import reverse
def student_login(request):
    message = None
    # print('request.user',request.user)
    if request.user.is_authenticated:
        return redirect("index")
    # 如果該email尚未被註冊

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        email_user = get_user_model().objects.filter(email=email).exists()
        if user is not None:
            login(request, user)
            return redirect("redirect_user")
        # 如果該email尚未被註冊
        elif email_user :
            message = "帳號或密碼錯誤"
        else:
            message = "該信箱尚未註冊"
    login_form = LoginForm()
    content = {"login_form": login_form, "message": message}
    
    return render(request, "login.html",content)