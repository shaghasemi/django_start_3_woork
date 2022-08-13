import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET","POST"])
def api_home(request, *args):
    model_data = Product.objects.all().order_by("?").first()
    print("sdasdasdasdasdsad")
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"])
        # json_data_str = json.dumps(data)
    return Response(data)
    # return JsonResponse(data)
    # return HttpResponse(json_data_str, headers={"Content-Type": "application/json"})
