from django.shortcuts import render
from django.http import response


# Create your views here.
def index(request):
    msg = {'status': "API UP!",
           'msg': "have a good day!"}
    return response.JsonResponse(msg)
