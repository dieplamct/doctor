import json
import urllib.parse

from django.http import HttpResponse
from django.views import View

class ViewWrapper(View):

    view_func = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())

        body, status = self.view_func(request, **kwargs).get(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        kwargs.update(json.loads(request.body))

        body, status = self.view_func(request, **kwargs).post(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def patch(self, request, *args, **kwargs):
        data = dict(urllib.parse.parse_qsl(request.body.decode("utf-8"), keep_blank_values=True))
        kwargs.update(data)

        body, status = self.view_func(request, **kwargs).patch(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        data = dict(urllib.parse.parse_qsl(request.body.decode("utf-8"), keep_blank_values=True))
        kwargs.update(data)

        body, status = self.view_func(request, **kwargs).delete(**kwargs)
        content = json.dumps(body) if body is not None else ''
        return HttpResponse(content, status=status, content_type='application/json')
