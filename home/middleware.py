from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if user is authenticated and is an admin
        if request.user.is_authenticated and request.user.is_superuser:
            if request.path == settings.LOGIN_URL or request.path == '/' or request.path == '/user'  or request.path == '/login' or request.path == '/reserve_car':
                return HttpResponseRedirect(reverse('administrator'))  # Redirect to admin dashboard URL
        
        if request.user.is_authenticated and not request.user.is_superuser:
            if request.path == settings.LOGIN_URL or request.path == '/' or request.path == '/administrator' or request.path == '/admin' or request.path == '/car_inventory' or request.path == '/login' or request.path == '/reservations' or request.path == '/approved_requests':
                return HttpResponseRedirect(reverse('user'))  # Redirect to admin dashboard URL

       
        # Check if the user is not authenticated
        if not request.user.is_authenticated:
            if request.path not in ['/','/login', '/register', '/about']:
            # Redirect to the login page
                return redirect(reverse('login'))  # Replace 'login' with your actual login URL name

        return response
