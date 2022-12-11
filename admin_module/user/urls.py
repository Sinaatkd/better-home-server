from django.urls import path

from .views import (AllUsersListView, CreateUserView, ConsultantUsersListView, UserUpdateView, ChangeUserPasswordUpdateView)


urlpatterns = [
    path('', AllUsersListView.as_view(), name='users_list'),
    path('consultants', ConsultantUsersListView.as_view(), name='consultant_users_list'),
    path('<int:pk>/detail', UserUpdateView.as_view(), name='user_detail'),
    path('<int:pk>/change-password', ChangeUserPasswordUpdateView.as_view(), name='user_change_password'),
    path('new', CreateUserView.as_view(), name='create_user'),
]