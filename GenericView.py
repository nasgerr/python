class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return " "

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods)

    def render_request(self, method, request):
        if method.upper() not in self.methods:
            raise TypeError()

        f = getattr(self, method.lower(), None)

        if f:
            return f(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError
        if 'url' not in request:
            raise TypeError

        return f"url: {request['url']}"

