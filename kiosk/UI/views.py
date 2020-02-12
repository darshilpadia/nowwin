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