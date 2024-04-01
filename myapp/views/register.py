from django.shortcuts import render,redirect
from myapp.forms import UserForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def register(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            password = user_form.cleaned_data.get('password')

            try:
                validate_password(password)
            except ValidationError as e:
                user_form.add_error('password', e)

            if user_form.errors:
                content = {"user_form": user_form}
                return render(request, "register.html", content)

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print("success")
            return redirect('/student_login')
    else:
        user_form = UserForm()

    content = {"user_form": user_form}
    return render(request, "register.html", content)