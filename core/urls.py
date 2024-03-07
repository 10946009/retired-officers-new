from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.shortcuts import render

# import views directly from the app
from myapp import urls as student_urls
from admin_panel import urls as admin_panel_urls
from admin_panel import urls as admin_panel_urls

def handler404(request, exception):
    if request.user.is_authenticated:
        print('True')
        return render(request, '404.html')
    else:
        print('Fail')
        return render(request, '1404.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',index.index,name="index"),
    # path('register/', register.register, name='register'),
    # path('login/', login.login, name='login'),
    path('', include(student_urls)),
    path('admin_panel/', include(admin_panel_urls)),
    # path('myapp/', include(myapp_urls)),

] 

handler404 = handler404
