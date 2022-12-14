from django.urls import path, include

from .views import (dashboard)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', include('admin_module.user.urls'), name='admin_user')
]