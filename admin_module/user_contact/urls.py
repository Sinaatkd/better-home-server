from django.urls import path

from .views import (DeleteUserContactView)


urlpatterns = [
    path('<int:pk>/delete', DeleteUserContactView.as_view(), name='user-contact-delete'),
]