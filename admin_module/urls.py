from django.urls import path, include

from .views import (dashboard)
from better_home_api import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout-admin'),
    path('users/', include('admin_module.user.urls'), name='admin-user'),
    path('estates/', include('admin_module.estate.urls'), name='admin-estate'),
]