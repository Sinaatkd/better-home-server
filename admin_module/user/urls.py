from django.urls import path

from .views import (AllUsersListView, CreateUserView, ConsultantUsersListView,
                    UserUpdateView, ChangeUserPasswordUpdateView, DeleteUserView, UserDetailView,
                    export_user_to_xlsx, move_consultant_estates_to_other_consultant)


urlpatterns = [
    path('', AllUsersListView.as_view(), name='users-list'),
    path('export-excel', export_user_to_xlsx, name='export-user-to-xlsx'),
    path('consultants', ConsultantUsersListView.as_view(), name='consultant-users-list'),
    path('<int:pk>/detail', UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/update', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete', DeleteUserView.as_view(), name='user-delete'),
    path('<int:pk>/change-password', ChangeUserPasswordUpdateView.as_view(), name='user-change-password'),
    path('<int:pk>/move-estate', move_consultant_estates_to_other_consultant, name='move-consultant-estates-to-other-consultant'),
    path('new', CreateUserView.as_view(), name='create-user'),
]