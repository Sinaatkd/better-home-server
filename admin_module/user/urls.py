from django.urls import path

from .views import (AllUsersListView, CreateUserView, ConsultantUsersListView,
                    UserUpdateView, ChangeUserPasswordUpdateView, export_user_to_xlsx)


urlpatterns = [
    path('', AllUsersListView.as_view(), name='users-list'),
    path('export-excel', export_user_to_xlsx, name='export-user-to-xlsx'),
    path('consultants', ConsultantUsersListView.as_view(), name='consultant-users-list'),
    path('<int:pk>/detail', UserUpdateView.as_view(), name='user-detail'),
    path('<int:pk>/change-password', ChangeUserPasswordUpdateView.as_view(), name='user-change-password'),
    path('new', CreateUserView.as_view(), name='create-user'),
]