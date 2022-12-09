class Application:

    def __init__(self, urlpattrns: dict, front_controller: list):
        self.urlpatterns = urlpattrns
        self.front_controller = front_controller

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path in self.urlpatterns:
            view = self.urlpatterns[path]

            request = {}

            for controller in self.front_controller:
              controller(request)
            code, text = view(request)

            start_response(code, [('Content-Type', 'text/html')])

            return [text.encode('utf-8')]

        else:
            # Если url нет в urlpatterns - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]