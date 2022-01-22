from django.shortcuts import render
from django.http import response
from django.core.mail import send_mail, EmailMultiAlternatives


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


def reply(request):

    # Setting up the content for the mail
    subject, from_email, to = 'hello', 'info@nutopia.in', ['marudhu2021@gmail.com', "rishimenonx@gmail.com"]
    text_content = 'This is an important message.'
    html_content = ""

    # getting the html generated
    template = render(request, 'msg.html')
    content = template.content.decode()

    # Creating and sending the mail
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(content, "text/html")
    msg.send()

    # Sending the response
    return response.JsonResponse({'status': 'success'})


def test(request):

    return render(request, 'mock.html', context={'val': request.GET['val']})
