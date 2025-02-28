#Import modules
from django.contrib import admin #Django admin module
from django.urls import path #URL routing
from authentication.views import * #Import views from the authentcation app
from django.conf import settings #Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #Static files serving

#Define url paths
urlpatterns = [
    path('admin/', admin.site.urls), #Home Page
    path("admin/", admin.site.urls), #Admin interface
    path('login/', login_page, name='login_page'), #Login Page
    path('register/', register_page, name='register'), #Registration page
]

#Serve media files if DEBUG is Trie (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns