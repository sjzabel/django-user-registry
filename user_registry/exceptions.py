class UserRegistryRegisterError(Exception):
    ''' There is already a user in the registry '''
    pass

class UserRegistryUnregisterError(Exception):
    ''' There is no user in the registry '''
    pass

class UserRegistryUnregisterWrongUserError(Exception):
    ''' There is the wrong user in the registry '''
    pass

