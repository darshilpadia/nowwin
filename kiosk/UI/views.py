from django.shortcuts import render, redirect
from API.views import *


# Create your views here.
def login(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        request.data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(request.data)
        r = Kiosk()
        re = r.Login(request)
        if re.data.get('result') == "Success":
            response = redirect('projects.html', permanent=True)
        return response

    else:
        return render(request, 'login.html', {})


def brandmaster(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'brandmaster.html', {})


def forgotpassword(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'forgot-password.html', {})