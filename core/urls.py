from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.shortcuts import render

# import views directly from the app
from myapp import urls as student_urls
from admin_panel import urls as admin_panel_urls
from admin_panel import urls as admin_panel_urls
from myapp.views import veteran
def handler404(request, exception):
    if request.user.is_authenticated:
        # print('True')
        return render(request, '404.html')
    else:
        # print('Fail')
        return render(request, '1404.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(student_urls)),
    # path('veteran/',include(student_urls)),

    path('admin_panel/', include(admin_panel_urls)),
    # path('accounts/', include('allauth.urls')),  # django-allauth網址
    path('403', TemplateView.as_view(template_name='403.html'), name='403'),
    
    # path("accounts/login/", RedirectView.as_view(pattern_name="index")),
    # path('myapp/', include(myapp_urls)),

] 

handler404 = handler404

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

