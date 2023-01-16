from django.urls import path


from .views import (EstateListView, EstateDeleteView, EstateCreateView, EstatePropertyCreateView,
                    EstateUpdateView, EstatePropertyListView, EstatePropertyDeleteView, EstatePropertyUpdateView)

urlpatterns = [
    path('', EstateListView.as_view(), name='estates-list'),
    path('<pk>/delete/', EstateDeleteView.as_view(), name='estate-delete'),
    path('<pk>/edit/', EstateUpdateView.as_view(), name='estate-edit'),
    path('new/', EstateCreateView.as_view(), name='create-estate'),
    path('properties/', EstatePropertyListView.as_view(), name='estate-property-list'),
    path('properties/new', EstatePropertyCreateView.as_view(), name='estate-property-create'),
    path('properties/<pk>/delete/', EstatePropertyDeleteView.as_view(), name='estate-property-delete'),
    path('properties/<pk>/update/', EstatePropertyUpdateView.as_view(), name='estate-property-update'),
]