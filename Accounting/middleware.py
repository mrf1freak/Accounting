import re
from django.http.response import HttpResponseRedirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)

        ALLOWED_URLS = [
            '/admin/',
            '/users/'
        ]

        if not request.user.is_authenticated:
            allowed_page = False
            for URL in ALLOWED_URLS:
                allowed_page = allowed_page or re.search("^" + URL + "*", request.path)

            if allowed_page:
                return response
            else:
                return HttpResponseRedirect('/users/login')

        
        return response