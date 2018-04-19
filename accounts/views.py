from django.core.urlresolvers import reverse
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.shortcuts import redirect
from accounts.models import Token
import os

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        os.environ.get('EMAIL_USER'),
        [email]
    )
    # send_mail(
    # 'Login link',
    # 'body text tbc',
    # 'email',
    # [email],
    # )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')
