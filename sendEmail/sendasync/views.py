from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response
#
from django.core.mail import send_mail
from django.conf import settings


class UserSendMail(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        current_user = request.user
        subject = 'Send from app DJ-CELERY-RABBIT'
        message = 'this is great, because is working its me: '+current_user.username
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['angel_one@yopmail.com',]
        send_mail(subject, message, email_from, recipient_list)

        return Response({'data': 'email sent'})
