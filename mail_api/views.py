from django.shortcuts import render
from django.http import response
from django.core.mail import send_mail


# Create your views here.
def index(request):
    msg = {'status': "API UP!",
           'msg': "have a good day!"}
    return response.JsonResponse(msg)


def mail(request):
    reciever = "marudhu2021@gmail.com"
    print("Sending mail")
    send_mail("Testing", "this is a test mail", "info@nutopia.in", [reciever])

    return response.JsonResponse({'status': 'success'})
