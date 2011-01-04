from django.contrib.auth.models import User
from django.conf import settings
from user_registry import UserRegistry
from user_registry.exceptions import UserRegistryNoSystemUserError

def as_system_user(pk=None):
    def _wrapper(func):
        user = None
        if pk:
            user = User.objects.get(pk=pk)
        else:
            if hasattr(settings,"USER_REGISTRY__SYSTEM_USER_ID"):
                user = User.objects.get(pk=settings.USER_REGISTRY__SYSTEM_USER_ID)

        if user:
            UserRegistry.register(user)
        else:
            raise UserRegistryNoSystemUserError()

        return func
    return _wrapper
