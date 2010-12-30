from user_registry import UserRegistry

class UserRegistryMiddleware(object):
    def process_request(self, request):
        print "UserRegistryMiddleware - process_request"
        user = self.get_user(request)
        if user:
            UserRegistry.register(user)

    
    def process_response(self, request, response):
        print "UserRegistryMiddleware - process_response"
        user = self.get_user(request)
        if user:
            UserRegistry.unregister(user)

        return response
    
    def get_user(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated():
            return request.user
        else:
            return None


