from django.urls import path


from .views import EstateListView, EstateDeleteView, EstateCreateView, EstateUpdateView, EstatePropertyListView

urlpatterns = [
    path('', EstateListView.as_view(), name='estates-list'),
    path('<pk>/delete/', EstateDeleteView.as_view(), name='estate-delete'),
    path('<pk>/edit/', EstateUpdateView.as_view(), name='estate-edit'),
    path('new/', EstateCreateView.as_view(), name='create-estate'),
    path('properties/', EstatePropertyListView.as_view(), name='estate-property-list'),
]