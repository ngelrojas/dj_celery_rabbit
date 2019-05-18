from django.conf import settings
from django.core.mail import send_mail


def task_send_email(current_user):
    try:
        subject = 'Send from app DJ-CELERY-RABBIT'
        message = 'this is great, because is working its me here now: ' + current_user.username
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['angel_one@yopmail.com', ]
        resp = send_mail(subject, message, email_from, recipient_list)
        return resp
    except Exception as err:
        return f'{err}'


def task_sum_user(current_user, x, y):
    # lookup user by id and send them a message
    resp_sum = x + y
    msg = 'the sum is: '+str(resp_sum)+' the user '+str(current_user.username)

    return msg
