from myapp.views.index import index
from myapp.views.register import register
from myapp.views.student_login import student_login
from myapp.views.logout import logout
from myapp.views.student_print_sign_up import student_print_sign_up
from myapp.views.student_print_score import student_print_score
from myapp.views.student_join import student_join
from django.urls import path , include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('student_login/', student_login, name='student_login'),
    path('logout/', logout, name='user_logout'),
    # about activity
    path('student_join/<int:activity_id>', student_join, name='student_join'),
    path('student_print_sign_up/<int:activity_id>', student_print_sign_up, name='student_print_sign_up'),
    path('student_print_score/<int:activity_id>', student_print_score, name='student_print_score'),
#     accounts/ password/reset/ [name='account_reset_password']
# accounts/ password/reset/done/ [name='account_reset_password_done']
# accounts/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
# accounts/ password/reset/key/done/ [name='account_reset_password_from_key_done']
    # path('password/reset',student_password_reset,name='student_password_reset'),
    path('accounts/password/reset',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('accounts/password/reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('accounts/password/reset/key/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('accounts/password/reset/key/done',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
