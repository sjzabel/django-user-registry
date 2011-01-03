from user_registry import UserRegistry

class UserRegistryMiddleware(object):
    def process_request(self, request):
        user = self.get_user(request)
        if user:
            UserRegistry.register(user, request)

    
    def process_response(self, request, response):
        user = self.get_user(request)
        if user:
            UserRegistry.unregister(user, request)

        return response
    
    def get_user(self, request):
        if hasattr(request, 'user'):
            return request.user
        return None


