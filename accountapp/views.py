from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

# 기존 장고 방식
def hello_world(request):
    return HttpResponse('Hello_World')

# DRF 방식
@api_view()
def hello_world_drf(request):
    return Response({"message": "hello_world"});