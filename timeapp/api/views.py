from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response

@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    if settings.DEBUG and request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': True, 'sessionId': request.session.session_key})
    return JsonResponse({'isAuthenticated': True})
