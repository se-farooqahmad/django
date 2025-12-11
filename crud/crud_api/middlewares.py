# custom_email_middleware.py
from django.conf import settings
from django.http import HttpResponseForbidden

class AllowedEmailDomainsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self.is_allowed(request):
            return self.get_response(request)
        else:
            return HttpResponseForbidden("Access Denied")

    def is_allowed(self, request):
        if request.path not in settings.DISALLOWED_API_ENDPOINT:
            return True

        user_email = request.user.email if request.user.is_authenticated else None
        email_domain = user_email.split('@')[-1] if user_email else None

        if email_domain in settings.ALLOWED_EMAIL_DOMAINS:
            return True
        return False
