from django.urls import path

from .views import (
    ClientCreateView,
    ClientListView,
    ClientRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<uuid:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-detail')
]