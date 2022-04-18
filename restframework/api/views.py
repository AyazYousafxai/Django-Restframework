import json
import re
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))

    body = request.body  # bytes string of json data
    print(body)
    data = {}
    # data = {
    #     'message': 'Hello API',
    #     'status': '200',
    # }
    try:
        data = json.loads(body)
    except:
        pass

    # print(data)
    data['params'] = dict(request.GET)
    data['header'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)