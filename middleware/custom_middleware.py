class CustomMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # request.hello = "examle text in django project"
        response = self.get_response(request)
        return response