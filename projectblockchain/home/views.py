
from django.core.mail import BadHeaderError
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pip._vendor.distlib.compat import raw_input


def send_email(request):
    print("welcome")
    subject =raw_input("enter subject")
    message =raw_input("enter message")

    if subject and message :
        try:
            send_mail(subject, message,'settings.EMAIL_HOST_USER', ['manureddy7143@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def index(request):
    return render(request, 'index.html')
