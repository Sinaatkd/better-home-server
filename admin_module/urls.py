from django.urls import path

from .views import (dashboard, AllUsersListView, CreateUserView, ConsultantUsersListView)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', AllUsersListView.as_view(), name='users_list'),
    path('users/consultants', ConsultantUsersListView.as_view(), name='consultant_users_list'),
    path('users/new', CreateUserView.as_view(), name='create_user'),
]