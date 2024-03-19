from myapp.views.index import index
from myapp.views.register import register
from myapp.views.student_login import student_login
from myapp.views.logout import logout
from myapp.views.student_join import student_join
from myapp.views.student_print_sign_up import student_print_sign_up
from myapp.views.student_print_score import student_print_score
from myapp.views.student_edit import student_edit
from myapp.views.student_password_reset import student_password_reset
from django.urls import path , include

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('student_login/', student_login, name='student_login'),
    path('logout/', logout, name='logout'),
    path('student_edit/', student_edit, name='student_edit'),
    # about activity
    path('student_join/<int:activity_id>', student_join, name='student_join'),
    path('student_print_sign_up/<int:activity_id>', student_print_sign_up, name='student_print_sign_up'),
    path('student_print_score/<int:activity_id>', student_print_score, name='student_print_score'),
#     accounts/ password/reset/ [name='account_reset_password']
# accounts/ password/reset/done/ [name='account_reset_password_done']
# accounts/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
# accounts/ password/reset/key/done/ [name='account_reset_password_from_key_done']
    # path('password/reset',student_password_reset,name='student_password_reset'),
    path('accounts/password/reset',include('django.contrib.auth.urls')),
    # path('accounts/password/reset',include('django.contrib.auth.urls')),
#------------------------------ 
    # path('create', views.create, name='create'),
    # path('list', views.list, name='list'),
    # path('fileupload', views.fileupload, name='fileupload'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('edit/update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('ajax/', views.ajax, name='ajax'),
    # path('ajax/ajax', views.ajax, name='ajaxpost'),
    # path('ajax/delete', views.ajax_delete, name='ajax_delete'),
    # path('ajax/getajax', views.getajax, name='getajax'),

    # path('register/success/', views.register_success, name='register_success'),
    # path('users/', views.users, name='users'),
    # path('users/delete/<int:id>', views.user_delete, name='user_delete'),
    # path('upload/csv/', views.upload_csv, name='upload_csv'),
    # path('change_password', views.changePassword, name='changePassword'),
    # path('file/delete', views.changePassword, name='changePassword'),
    # path('file/delete/<int:id>', views.deleteFiles, name='deleteFiles'),

]
