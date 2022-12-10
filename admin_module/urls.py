from django.urls import path

from .views import (dashboard, AllUsersListView, CreateUserView, ConsultantUsersListView, UserUpdateView, ChangeUserPasswordUpdateView)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', AllUsersListView.as_view(), name='users_list'),
    path('users/consultants', ConsultantUsersListView.as_view(), name='consultant_users_list'),
    path('user/<int:pk>/detail', UserUpdateView.as_view(), name='user_detail'),
    path('user/<int:pk>/change-password', ChangeUserPasswordUpdateView.as_view(), name='user_change_password'),
    path('users/new', CreateUserView.as_view(), name='create_user'),
]