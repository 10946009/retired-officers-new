from myapp.views.index import index
from myapp.views.register import register
from myapp.views.student_login import student_login
from myapp.views.logout import logout
from myapp.views.student_print import student_print_sign_up,student_print_score
from myapp.views.api_data import api_student_print_sign_up, api_student_print_score
from myapp.views.student_join import student_join
from myapp.views.password_reset import PasswordReset
from myapp.views.veteran import veteran,not_open
from django.urls import path , include
from django.contrib.auth import views as auth_views
urlpatterns = [
        #test...
    # path('',not_open),
    # path('veteran',not_open,name='veteran'),
    #test...
    # path('2BkSDAqYaRhXRfIU', index, name='index'),
    # 正式
    path('', veteran, name='veteran'),
    path('veteran', index, name='index'),
    path('register/', register, name='register'),
    path('student_login/', student_login, name='student_login'),
    path('logout/', logout, name='user_logout'),
    # about activity
    path('student_join/<int:activity_id>', student_join, name='student_join'),
    path('student_print_sign_up/<int:activity_id>', student_print_sign_up, name='student_print_sign_up'),
    path('student_print_score/<int:activity_id>', student_print_score, name='student_print_score'),

    # api get data
    path('api/student_print_sign_up', api_student_print_sign_up, name='api_student_print_sign_up'),
    path('api/student_print_score', api_student_print_score, name='api_student_print_score'),

    # google login
    # path('accounts/google/login/', include(google_urlpatterns)),
    #socialaccount_login
    # ...
    path('accounts/password/reset/',PasswordReset.as_view(template_name="password_reset.html", email_template_name = 'password_reset_email.html'),name='password_reset'),
    path('accounts/password/reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('accounts/password/reset/key/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('accounts/password/reset/key/done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    # google login
    path('accounts/', include('allauth.socialaccount.providers.google.urls')),
    #social/ google/
    #social/ google/login/token/ [name='google_login_by_token']
]
