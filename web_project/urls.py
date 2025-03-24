# Import necessary modules
from django.contrib import admin  
from django.urls import path  
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
from django.contrib import admin
from django.urls import path
from users.views import home, login_page, register_page, logout_view, profile_view
# Import views
from users.views import home, login_page, register_page, logout_view, profile_view  
from users.views import create_event, update_event, delete_event  

# Define URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path('home/', home, name="home"),  # Home page
    path('login/', login_page, name='login_page'),  # Login page
    path('register/', register_page, name='register'),  # Registration page
    path('logout/', logout_view, name='logout'),  # Logout page
    path('profile/', profile_view, name='profile'),  # Profile page
    
    # Event CRUD URLs
    path('event/create/', create_event, name='create_event'),
    path('event/update/<int:event_id>/', update_event, name='update_event'),
    path('event/delete/<int:event_id>/', delete_event, name='delete_event'),
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files
urlpatterns += staticfiles_urlpatterns()
