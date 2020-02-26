from django.shortcuts import render, redirect
from API.views import *


def login(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        request.data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(request.data)
        r = Kiosk()
        re = r.Login(request)
        if re.data.get('result') == "Success":
            response = redirect('dashboard', permanent=True)
        elif re.data.get('result') == "Forbidden":
            response = render(request, 'login.html', {'flag': '1'})
        else:
            response = render(request, 'login.html', {'flag': '0'})
        print(response)
        return response

    else:
        return render(request, 'login.html', {'flag': '0'})


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


def brandmaster(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        if request.POST.get('brandid') is not None:
            request.data = {'BrandID': request.POST.get('brandid'), 'BrandName': request.POST.get('brandname')}
            r = Kiosk()
            if int(request.data.get('BrandID')) > 0:
                res = r.update_BrandMaster(request)
            else:
                res = r.ins_BrandMaster(request)
            if res.data.get('result') == 'Success':
                response = redirect('brandview', permanent=True)
            return response
        else:
            request.data = {'brand_name': request.POST.get('brandname')}
            r = Kiosk()
            res = r.ins_BrandMaster(request)
            print(res)
            if res.data.get('result') == 'Success':
                response = redirect('brandview', permanent=True)
            return response
    else:
        data = {'BrandID': 0, 'BrandName': ''}
        return render(request, 'brandmaster.html', {'data': data})


def del_brandmasterbyid(request, brand_id):
    print('------', request.POST)
    print('------', request)
    if request.method == "GET":
        request.data = {'BrandID': brand_id}
        r = Kiosk()
        res = r.get_BrandByID(request)
        print(res)
        if res.data.get('result') == 'Success':
            data = res.data.get('data')
            response = redirect('brandview', permanent=True)
            return response
    else:
        response = redirect('brandview', permanent=True)
        return response


def brandmasterbyid(request, brand_id):
    print('------', request.POST)
    print('------', request)
    if request.method == "GET":
        request.data = {'BrandID': brand_id}
        r = Kiosk()
        res = r.get_BrandByID(request)
        print(res)
        if res.data.get('result') == 'Success':
            data = res.data.get('data')
            return render(request, 'brandmaster.html', {'data': data})
        # return response
    else:
        data = {'BrandID': 0, 'BrandName': ''}
        return render(request, 'brandmaster.html', {'data': data})


def devicemaster(request):
    print('------******************', request.POST)
    print('------', request)
    if request.method == "POST":
        request.data = {'DeviceNumber': request.POST.get('devicenumber'), 'DeviceMac': request.POST.get('devicemac'),
                        'DeviceAddress': request.POST.get('deviceaddress'),
                        'City': request.POST.get('city'),
                        'State': request.POST.get('state'), 'DeviceID': request.POST.get('DeviceID')
                        }
        print(request.POST.get('DeviceID'))
        r = Kiosk()
        if request.POST.get('DeviceID') is not '':
            print('in update')
            res = r.update_Device(request)
        else:
            print('in ins')
            res = r.ins_DeviceMaster(request)
        print(res)
        if res.data.get('result') == 'Success':
            response = redirect('deviceview', permanent=True)
        return response
    else:
        return render(request, 'devicemaster.html', {})


def devicemasterbyid(request, device_id):
    print('------', request.POST)
    print('------', request)
    if request.method == "GET":
        request.data = {'DeviceID': device_id}
        r = Kiosk()
        res = r.get_DeviceByID(request)
        print(res)
        if res.data.get('result') == 'Success':
            data = res.data.get('data')
            return render(request, 'devicemaster.html', {'data': data})
        # return response
    else:
        data = {'DeviceID': 0, 'DeviceNumber': '', 'City': '', 'State': '', 'DeviceAddress': '', 'DeviceMac': ''}
        return render(request, 'brandmaster.html', {'data': data})


def modelmaster(request):
    print('------model masert ----', request.POST)
    print('------', request)
    if request.method == "POST":
        request.data = {'modelname': request.POST.get('modelname'), 'ram': request.POST.get('ram'),
                        'brandid': int(request.POST.get('brandid')),
                        'price': request.POST.get('price'),
                        'back_camera1': request.POST.get('back_camera1'),
                        'back_camera2': request.POST.get('back_camera2'),
                        'back_camera3': request.POST.get('back_camera3'),
                        'back_camera4': request.POST.get('back_camera4'),
                        'back_camera5': request.POST.get('back_camera5'),
                        'front_camera1': request.POST.get('front_camera1'),
                        'front_camera2': request.POST.get('front_camera2'),
                        'front_camera3': request.POST.get('front_camera3'),
                        'front_camera4': request.POST.get('front_camera4'),
                        'screen_size': request.POST.get('screen_size'),
                        'sim_type': request.POST.get('sim_type'),
                        'expandable_storage': request.POST.get('expandable_storage'),
                        'color1': request.POST.get('color1'),
                        'color2': request.POST.get('color2'), 'color3': request.POST.get('color3'),
                        'color4': request.POST.get('color4'), 'color5': request.POST.get('color5'),
                        'color6': request.POST.get('color6'), 'color7': request.POST.get('color7'),
                        'cpudtl': request.POST.get('cpu_details'), 'osdtl': request.POST.get('os_details'),
                        'bdtl': request.POST.get('battery_details'), 'fingerprint': request.POST.get('fingerprints'),
                        'back_flashlight': True if request.POST.get('backflash') == 'on' else False,
                        'front_flashlight': True if request.POST.get('frontflash') == 'on' else False,
                        'ModelID': request.POST.get('ModelID'),
                        'storage': request.POST.get('storage'),
                        'processor': request.POST.get('processor'), 'modeldtlid': request.POST.get('modeldtlid')

                        }
        r = Kiosk()
        if request.POST.get('ModelID') is not '0':
            res = r.update_Model(request)
        else:
            print('in else')
            res = r.ins_ModelMaster(request)
            print('im back')
            request.data['ModelID'] = res.data.get('ModelID')
            print('going to update')
            res_dtl = r.ins_ModelDTL(request)
        if res.data.get('result') == 'Success' and res_dtl.data.get('result') == 'Success':
            response = redirect('modelview', permanent=True)
        return response
    else:
        r = Kiosk()
        res = r.get_BrandView(request)
        data = res.data.get('data')
        form_data = {'ModelID': 0, 'ModelName': '',
                     'BrandID': '', 'isactive': '',
                     'ModelDTLID': '', 'RAM': '',
                     'Storage': '', 'price': '',
                     'back_camera1': '', 'back_camera2': '',
                     'back_camera3': '', 'back_camera4': '',
                     'back_camera5': '', 'front_camera1': '',
                     'front_camera2': '', 'front_camera3': '',
                     'front_camera4': '', 'screen_size': '',
                     'SIM_type': '', 'expandable_storage': '',
                     'color1': '', 'color2': '',
                     'color3': '', 'color4': '',
                     'color5': '', 'color6': '',
                     'color7': '', 'processor': '',
                     'osdtl': '', 'bdtl': '',
                     'fingerprint': '', 'back_flashlight': '',
                     'front_flashlight': '', 'fc_count': 0, 'bc_count': 0}
        return render(request, 'modelmaster.html', {'d': data, 'form_data': form_data})


def modelview(request):
    print('------', request.POST)
    print('------**************', request)
    r = Kiosk()
    # b_d = r.get_BrandView(request)
    m_d = r.get_ModelView(request)
    if m_d.data.get('result') == 'Success':
        # brand_data = b_d.data.get('data')
        model_data = m_d.data.get('data')
        print(model_data)
        return render(request, 'modelview.html', {'m_d': model_data})
    else:
        return render(request, 'modelview.html', {})


def modelmasterbyid(request, model_id):
    print('------', request.POST)
    print('------', request)
    if request.method == "GET":
        request.data = {'ModelID': model_id}
        r = Kiosk()
        res = r.get_ModelByID(request)
        print(res)
        res_brand = r.get_BrandView(request)
        if res.data.get('result') == 'Success':
            print(res.data.get('data'))
            form_data = res.data.get('data')
            data = res_brand.data.get('data')
            return render(request, 'modelmaster.html', {'d': data, 'form_data': form_data})
        # return response
    else:
        data = {'ModelID': 0, 'ModelName': None,
                'BrandID': None, 'isactive': None,
                'ModelDTLID': None, 'RAM': None,
                'Storage': None, 'price': None,
                'back_camera1': None, 'back_camera2': None,
                'back_camera3': None, 'back_camera4': None,
                'back_camera5': None, 'front_camara1': None,
                'front_camara2': None, 'front_camara3': None,
                'front_camara4': None, 'screen_size': None,
                'SIM_type': None, 'expandable_storage': None,
                'color1': None, 'color2': None,
                'color3': None, 'color4': None,
                'color5': None, 'color6': None,
                'color7': None, 'processor': None,
                'osdtl': None, 'bdtl': None,
                'fingerprint': None, 'back_flashlight': None,
                'front_flashlight': None, 'fc_count': 0, 'bc_count': 0}
        return render(request, 'brandmaster.html', {'data': data})


def deviceview(request):
    print('------', request.POST)
    print('------**************', request)
    r = Kiosk()
    # b_d = r.get_BrandView(request)
    m_d = r.get_DeviceView(request)
    if m_d.data.get('result') == 'Success':
        # brand_data = b_d.data.get('data')
        device_data = m_d.data.get('data')
        print(device_data)
        return render(request, 'deviceview.html', {'d_d': device_data})
    else:
        return render(request, 'modelview.html', {})


def dashboard(request):
    r = Kiosk()
    d_d = r.get_DashbordData(request)
    if d_d.data.get('result') == 'Success':
        print(d_d.data.get('data'))
        return render(request, 'dashboard.html', {'d_d': d_d.data.get('data')})


def reportview(request):
    return render(request, 'reports.html')

def generalreport(request):
    r = Kiosk()
    res = r.get_general_excel(request)
    return res

def forgotpassword(request):
    print('------', request.POST)
    print('------', request)
    if request.method == "POST":
        data = {'EmailID': request.POST.get('EmailID'), 'Password': request.POST.get('Password')}
        print(data)
    else:

        return render(request, 'forgot-password.html', {})


def del_modelmasterbyid(request, model_id1):
    print('------', request.POST)
    print('------*************************************model del', request)
    if request.method == "GET":
        request.data = {'ModelID': model_id1}
        r = Kiosk()
        res = r.del_ModelMaster(request)
        print(res)
        if res.data.get('result') == 'Success':
            data = res.data.get('data')
            response = redirect('modelview', permanent=True)
            return response
    else:
        response = redirect('brandview', permanent=True)
        return response
