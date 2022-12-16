from django.urls import path


from .views import GetAuthenticatedUserAPI

urlpatterns = [
    path('', GetAuthenticatedUserAPI.as_view(), name='get-authenticated-user-api'),
]