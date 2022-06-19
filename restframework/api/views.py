import json
import re
from products.models import Product
from django.http import JsonResponse,HttpResponse
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # if request.method != "POST":
    #     return Response({"Details":"GET method not allowed"}, status=405)
    instance=Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # instance = model_to_dict(model_data,fields=['id','content','title','price','saleprice'])
        data = ProductSerializer(instance).data
        # data_json_str = json.dumps(data)
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content']=model_data.content
    #     data['price']=model_data.price
    return Response(data) # return json data
    # return HttpResponse(data_json_str, headers={"content-type":"application/json"}) # return string data, it show error on decimal data