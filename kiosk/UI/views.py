from django.shortcuts import render


# Create your views here.
def login(request):
    print('------',request.POST)
    print('------',request)
    if request.method == "POST":
        return render(request, 'index.html', {})
    else:
        return render(request, 'login.html',{})
