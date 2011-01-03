from user_registry.exceptions import UserRegistryRegisterError, UserRegistryUnregisterError, UserRegistryUnregisterWrongUserError
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from django.contrib.auth.models import AnonymousUser

class UserRegistry(object):
    '''
    singleton object to hold on to the request user
    for use in models & signals

    doing this for a wsgi stack... no idea of how it would work in a multithreaded environment

    note: maybe allow Anon Users
    note: maybe allow for Default System User
    '''
    _user = None

    @classmethod
    def register(klass,user,request):
        '''
        _user should always None else raise error
        '''
        print 'register'
        if klass._user:
            raise UserRegistryRegisterError()

        klass._user = user

    @classmethod
    def logged_in_register(klass,user,request):
        '''
        _user should always None else raise error
        '''
        print 'logged_in_register'
        print user
        print klass._user
        print klass._user == user
        if klass._user and klass._user.is_authenticated():
            raise UserRegistryRegisterError()

        klass._user = user

    @classmethod
    def unregister(klass,user,request):
        '''
        _user should not be None else raise error
        '''
        print 'unregister'
        print user
        if not klass._user:
            raise UserRegistryUnregisterError()

        if not klass._user == user:
            raise UserRegistryUnregisterWrongUserError()

        klass._user = None

    @classmethod
    def logged_out_unregister(klass,user,request):
        '''
        _user should always None else raise error
        '''
        print 'logged_out_unregister'
        print user
        print klass._user
        print klass._user == user
        if not (klass._user and klass._user == user):
            raise UserRegistryRegisterError()

        klass._user = AnonymousUser()

    @classmethod
    def has_user(klass):
        return klass._user != None
        
    @classmethod
    def get_user(klass):
        return klass._user

@receiver(user_logged_in, dispatch_uid="user_registry_user_logged_in")
def user_logged_in_receiver(sender,**kwargs):
    '''
    The signal of when a user logs in

    If there is an existing Anon user we can change it out for the correct user
    '''
    print 'logged in receiver'
    user = kwargs['user']
    request = kwargs['request']
    UserRegistry.logged_in_register(user,request)


@receiver(user_logged_out, dispatch_uid="user_registry_user_logged_in")
def user_logged_out_receiver(sender,**kwargs):
    '''
    The signal of when a user logs out

    If there is an existing user, we can change it out for an anon user
    '''
    print 'logged out receiver'
    user = kwargs['user']
    request = kwargs['request']
    UserRegistry.logged_out_unregister(user,request)

