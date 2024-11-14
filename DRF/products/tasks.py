from __future__ import absolute_import,unicode_literals
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
@shared_task
def send_email(subject, message,recipient_list):
    send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)