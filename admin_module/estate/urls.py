from django.urls import path


from .views import EstateListView

urlpatterns = [
    path('', EstateListView.as_view(), name='estates-list'),
]