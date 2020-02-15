from django.shortcuts import render, redirect
from API.views import *


# Create your views here.
def login(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'login.html', {})


def brandmaster(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        request.data = {'brand_name': request.POST.get('brandname')}
        r = Kiosk()
        res = r.ins_BrandMaster(request)
        print(res)
        if res.data.get('result') == 'Success':
            response = redirect('brandview.html', permanent=True)
        return response
    else:
        return render(request, 'brandmaster.html', {})


def modelmaster(request):
    print('------model masert ----', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'modelmaster.html', {})
