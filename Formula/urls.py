from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import register, user_login, user_logout, profile, profile_update

from home.views import home_page
from nevskiy.views import nevskiy
from zakaz.views import zakaz

urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),
    path('', home_page, name='home_page'),
    path('nevskiy', nevskiy, name='nevskiy'),
    path('zakaz', zakaz, name='zakaz'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('profile', profile, name='profile'),
    path('profile/update/<int:id>/', profile_update, name='profile_update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
