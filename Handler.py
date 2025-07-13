class Handler:
    def __init__(self, methods=('GET', )):
        self.__methods = methods
    def call(self, func):
        def wrapper(request):
            m = request.get('method', 'GET')
            if m in self.__methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper
    def get(self, func, request):
        return f'GET: {func(request)}'
    def post(self, func, request):
        return f'POST: {func(request)}'

