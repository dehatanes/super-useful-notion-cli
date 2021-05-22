from sunc.settings import VALID_REQUEST_METHODS

class RequestMethodException(IOError):
    def __init__(self, method):
        self.method = method
        self.message = 'The accepted methods are one of the following %s. %s is not accpted' % (','.join(VALID_REQUEST_METHODS), method)
