from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
    # Include app-level URLs from the users app
    path('', include('users.urls')),
]
