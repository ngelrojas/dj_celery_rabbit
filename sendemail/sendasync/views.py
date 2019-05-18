from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response
from .tasks import task_send_email, task_sum_user


class UserSendMail(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            current_user = request.user
            #
            # task_send_email(current_user)
            #
            task_sum_user(current_user, 4, 5)

            return Response({'data': True, 'msg': 'email sent'})

        except Exception as error:
            return Response({'data': f'{error}', 'msg': 'error'})

