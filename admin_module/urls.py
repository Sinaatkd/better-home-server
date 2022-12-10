from django.urls import path

from .views import dashboard, AllUsersListView

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('users/', AllUsersListView.as_view(), name='users-list'),
]