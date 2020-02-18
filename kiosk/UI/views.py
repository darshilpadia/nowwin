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
        request.data = {'modelname': request.POST.get('modelname'), 'RAM': request.POST.get('ram'),
                        'price': request.POST.get('price'),
                        'back_camera1': request.POST.get('back_camera1'),
                        'back_camera2': request.POST.get('back_camera2'),
                        'back_camera3': request.POST.get('back_camera3'),
                        'back_camera4': request.POST.get('back_camera4'),
                        'back_camera5': request.POST.get('back_camera15'),
                        'front_camara1': request.POST.get('front_camara1'),
                        'front_camara2': request.POST.get('front_camara2'),
                        'front_camara3': request.POST.get('front_camara3'),
                        'front_camara4': request.POST.get('front_camara4'),
                        'screen_size': request.POST.get('screen_size'),
                        'SIM_type': request.POST.get('SIM_type'),
                        'expandable_storage': request.POST.get('expandable_storage'),
                        'color1': request.POST.get('color1'),
                        'color2': request.POST.get('color2'), 'color3': request.POST.get('color3'),
                        'color4': request.POST.get('color4'), 'color5': request.POST.get('color5'),
                        'color6': request.POST.get('color6'), 'color7': request.POST.get('color7'),
                        'cpudtl': request.POST.get('cpudtl'), 'osdtl': request.POST.get('osdtl'),
                        'bdtl': request.POST.get('bdtl'), 'fingerprint': request.POST.get('fingerprint'),
                        'back_flashlight': request.POST.get('back_flashlight'),
                        'front_flashlight': request.POST.get('front_flashlight'),

                        }
        r = Kiosk()
        res = r.ins_ModelMaster(request)
        if res.data.get('result') == 'Success':
            response = redirect('modelview.html', permanent=True)
        return response
    else:
        return render(request, 'modelmaster.html', {})


def brandview(request):
    print('------', request.POST)
    print('------', request)
    r = Kiosk()
    b = r.get_BrandView(request)
    if b.data.get('result') == 'Success':
        data = b.data.get('data')
        print(data)
        return render(request, 'brandview.html', {'d': data})
    else:
        return render(request, 'brandview.html', {})


def modelview(request):
    print('------', request.POST)
    print('------**************', request)
    r = Kiosk()
    # b_d = r.get_BrandView(request)
    m_d = r.get_ModelView(request)
    if m_d.data.get('result') == 'Success':
        # brand_data = b_d.data.get('data')
        model_data = m_d.data.get('data')
        # print(brand_data)
        return render(request, 'modelview.html', {'m_d': model_data})
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


def forgotpassword(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:

        return render(request, 'forgot-password.html', {})
