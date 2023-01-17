from django.urls import path


from .views import (EstateListView, EstateDeleteView, EstateCreateView, EstatePropertyCreateView, EstateDetailView,
                    EstateUpdateView, EstatePropertyListView, EstatePropertyDeleteView, EstatePropertyUpdateView,
                    EstateRegionListView, EstateRegionDeleteView, EstateRegionCreateView, EstateRegionUpdateView,
                    EstateImageDeleteView,)

urlpatterns = [
    path('', EstateListView.as_view(), name='estates-list'),
    path('<pk>/detail/', EstateDetailView.as_view(), name='estates-detail'),
    path('<pk>/delete/', EstateDeleteView.as_view(), name='estates-delete'),
    path('<pk>/edit/', EstateUpdateView.as_view(), name='estates-update'),
    path('new/', EstateCreateView.as_view(), name='create-estate'),
    
    path('properties/', EstatePropertyListView.as_view(), name='estate-property-list'),
    path('properties/new', EstatePropertyCreateView.as_view(), name='estate-property-create'),
    path('properties/<pk>/delete/', EstatePropertyDeleteView.as_view(), name='estate-property-delete'),
    path('properties/<pk>/update/', EstatePropertyUpdateView.as_view(), name='estate-property-update'),

    path('regions/', EstateRegionListView.as_view(), name='estate-region-list'),
    path('regions/<pk>/delete/', EstateRegionDeleteView.as_view(), name='estate-region-delete'),
    path('regions/new', EstateRegionCreateView.as_view(), name='estate-region-create'),
    path('regions/<pk>/update/', EstateRegionUpdateView.as_view(), name='estate-region-update'),

    path('<estate_id>/images/<pk>/delete/', EstateImageDeleteView.as_view(), name='estate-image-delete'),


]