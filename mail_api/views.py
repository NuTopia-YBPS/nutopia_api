import json
from django.http import response
from django.shortcuts import render
from rest_framework import permissions
from django.core.mail import EmailMultiAlternatives
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def reply(request):

    # making sure to respond to post requests alone
    if request.method == "POST":

        serialized = request.data

        # Setting up the content for the mail
        to = serialized['recipients']
        subject = 'Registration Was Successful!'
        from_email = '"NuTopia" <info@nutopia.in>'
        text_content = 'Thank You! Your Registration Was Successful!'

        # context data
        context = {'isTeam': serialized['isTeam'],
                   'participants': serialized['participants'],
                   'event': serialized['event']}
        
        if context['isTeam'] == True:
            context['teamName'] = serialized['teamName']
        else:
            context['teamName'] = None


        # getting the html generated
        template = render(request, 'main.html', context=context)
        content = template.content.decode()

        # Creating and sending the mail
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(content, "text/html")
        msg.send()

    # Sending the response
    return response.JsonResponse({'status': 'success'})
