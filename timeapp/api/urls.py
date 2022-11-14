from django.urls import path, include

from .views import get_csrf, session_view

urlpatterns = [
    path('csrf/', get_csrf, name='get-csrf'),
    path('session/', session_view, name='session-view'),
    path('api-auth/', include('rest_framework.urls')),
]