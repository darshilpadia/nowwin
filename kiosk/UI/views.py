from django.shortcuts import render


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
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'brandmaster.html', {})

def brandview(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'brandview.html', {})

def modelview(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'modelview.html', {})

def deviceview(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'deviceview.html', {})

def userview(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:
        return render(request, 'userview.html', {})
