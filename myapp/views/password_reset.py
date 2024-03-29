from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.core.exceptions import ValidationError

class PasswordReset(auth_views.PasswordResetView):
    def form_valid(self, form):
            User = get_user_model()
            email = form.cleaned_data.get('email')
            if not User.objects.filter(email=email).exists():
                form.add_error('email', ValidationError('此電子郵件地址未註冊'))
                return self.form_invalid(form)
            return super().form_valid(form)