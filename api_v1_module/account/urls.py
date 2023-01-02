from django.urls import path


from .views import (GetAuthenticatedUserAPI, GetFavEstatesAPI, RemoveFromUserEstateFavAPI,
                    AddToUserEstateFavAPI)

urlpatterns = [
    path('', GetAuthenticatedUserAPI.as_view(), name='get-authenticated-user-api'),
    path('fav-estates/', GetFavEstatesAPI.as_view(), name='get-fav-estates-api'),
    path('fav-estates/add/', AddToUserEstateFavAPI.as_view(), name='add-to-user-estates-fav-api'),
    path('fav-estates/remove/', RemoveFromUserEstateFavAPI.as_view(), name='remove-from-user-estates-fav-api'),
]