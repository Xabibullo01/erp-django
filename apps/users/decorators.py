from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def role_required(*roles):
    def decorator(view):
        @login_required
        def _wrapped(request, *a, **kw):
            if request.user.is_superuser or request.user.role in roles:
                return view(request, *a, **kw)
            return HttpResponseForbidden("Ruxsat yo‘q")

        return _wrapped

    return decorator
