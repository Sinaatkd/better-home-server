from django.urls import path


from .views import EstateListView, EstateDeleteView, EstateCreateView

urlpatterns = [
    path('', EstateListView.as_view(), name='estates-list'),
    path('<pk>/delete/', EstateDeleteView.as_view(), name='estate-delete'),
    path('new/', EstateCreateView.as_view(), name='create-estate'),
]