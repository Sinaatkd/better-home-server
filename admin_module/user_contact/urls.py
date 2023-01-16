from django.urls import path

from .views import (DeleteUserContactView, CreateUserContactView)


urlpatterns = [
    path('<int:consultant_id>/new/', CreateUserContactView.as_view(), name='user-contact-create'),
    path('<int:pk>/delete', DeleteUserContactView.as_view(), name='user-contact-delete'),
]