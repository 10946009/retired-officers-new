from myapp.views.index import index
from myapp.views.register import register
from myapp.views.student_login import student_login
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('student_login', student_login, name='student_login'),
    # about activity
    path('student_join',)
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
