from django.urls import path


from .views import GetAuthenticatedUserAPI, GetFavEstatesAPI

urlpatterns = [
    path('', GetAuthenticatedUserAPI.as_view(), name='get-authenticated-user-api'),
    path('fav-estates', GetFavEstatesAPI.as_view(), name='get-fav-estates-api'),
]