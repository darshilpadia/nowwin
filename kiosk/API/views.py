from django.shortcuts import render
import uuid
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Create your views here.


class Utils():
    def VerifyUser(self, userid, token):
        try:
            verify_obj = UserActiveLogon.objects.get(UserID=userid, Token=token)
            if verify_obj.IsActive:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False

    def VerifyKiosk(self, kioskid, token):
        try:
            verify_obj = DeviceMaster.objects.get(DeviceID=kioskid, Token=token)
            if verify_obj.IsActive:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False


class Kiosk(ModelViewSet):
    queryset = BrandMaster.objects.all()
    serializer_class = BrandMasterSerializer

    # KIOSK
    @action(methods=['POST'], detail=False)
    def getmyid(self, request):
        print('--', request.data)
        try:
            device_obj = DeviceMaster.objects.get(Devicemac=request.data.get('mac'))
            data = {'DeviceID': device_obj.DeviceID}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Here is your id', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def ins_DeviceMaster(self, request):
        print('--', request.data)
        try:
            ins_obj = DeviceMaster.objects.create(
                DeviceNumber=request.data.get('device_number'),
                DeviceAddress=request.data.get('device_address'),
                City=request.data.get('city'),
                State=request.data.get('state'),
                DeviceMac=request.data.get('device_mac'),

            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added', }
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def ins_DeviceDTL(self, request):
        print('--', request.data)
        try:
            ins_obj = DeviceDTL.objects.create(
                DeviceID=request.data('deviceid'),
                ModelID=request.data('modelid'),
                TotalScreenTime=request.data('total_screen_time'),
                CameraClick=request.data('camera_click'),
                RAMClick=request.data('ram_click'),
                StorageClick=request.data('storage_click'),
                OtherClick=request.data('other_click'),

            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added', }
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def ins_BrandMaster(self, request):
        print('--', request.data)
        try:
            ins_obj = BrandMaster.objects.create(
                BrandName=request.data.get('brand_name')
            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added', }
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # KIOSK
    @action(methods=['POST'], detail=False)
    def get_VerificationCode(self, request):
        print('--', request.data)
        try:
            pass
        except Exception as e:
            print(str(e))

    @action(method=['POST'], detail=False)
    def get_BrandView(self, request):
        print('--', request.data)
        try:
            brand_view_obj = BrandMaster.objects.filter()
            data = {'brand_list', brand_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Brand', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)

    @action(method=['POST'], detail=False)
    def get_ModelView(self, request):
        print('--', request.data)
        try:
            model_view_obj = ModelMaster.ojects.filter(isactive=True)
            data = {'model_list', model_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Model', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)

    @action(method=['POST'], detail=False)
    def get_UserView(self, request):
        print('--', request.data)
        try:
            user_view_obj = UserMaster.objects.filter(IsActive=True)
            data = {'user_list', user_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of User', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)

    @action(method=['POST'], detail=False)
    def get_DeviceView(self, request):
        print('--', request.data)
        try:
            device_view_obj = DeviceMaster.objects.filter(isactive=True)
            data = {'device_list', device_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of device', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def get_BrandView(self, request):
        print('--', request.data)
        try:
            brand_view_obj = BrandMaster.objects.filter()
            data = {'brindlist': brand_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List Of Brand', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def get_BrandByID(self, request):
        print('--', request.data)
        try:
            brand_view_obj = BrandMaster.objects.get(BrandID=request.data.get('BrandID'))
            data = {'BrandID': brand_view_obj.BrandID, 'BrandName': brand_view_obj.BrandName}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of Brand', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def get_ModelByID(self, request):
        print('--', request.data)
        try:
            model_view_obj = ModelMaster.objects.get(ModelID=request.data.get('ModelID'))
            modeldtl_view_obj = ModelDTL.objects.get(ModelID=request.data.get('ModelID'))
            data = {'ModelID': model_view_obj.ModelID, 'ModelName': model_view_obj.ModelName,
                    'BrandID': model_view_obj.BrandID, 'isactive': model_view_obj.isactive,
                    'ModelDTLID': modeldtl_view_obj.ModelDTLID, 'RAM': modeldtl_view_obj.RAM,
                    'Storage': modeldtl_view_obj.Storage, 'price': modeldtl_view_obj.price,
                    'back_camera1': modeldtl_view_obj.back_camera1, 'back_camera2': modeldtl_view_obj.back_camera2,
                    'back_camera3': modeldtl_view_obj.back_camera3, 'back_camera4': modeldtl_view_obj.back_camera4,
                    'back_camera5': modeldtl_view_obj.back_camera5, 'front_camara1': modeldtl_view_obj.front_camara1,
                    'front_camara2': modeldtl_view_obj.front_camara2, 'front_camara3': modeldtl_view_obj.front_camara3,
                    'front_camara4': modeldtl_view_obj.front_camara4, 'screen_size': modeldtl_view_obj.screen_size,
                    'SIM_type': modeldtl_view_obj.SIM_type, 'expandable_storage': modeldtl_view_obj.expandable_storage,
                    'color1': modeldtl_view_obj.color1, 'color2': modeldtl_view_obj.color2,
                    'color3': modeldtl_view_obj.color3, 'color4': modeldtl_view_obj.color4,
                    'color5': modeldtl_view_obj.color5, 'color6': modeldtl_view_obj.color6,
                    'color7': modeldtl_view_obj.color7, 'processor': modeldtl_view_obj.processor,
                    'osdtl': modeldtl_view_obj.osdtl, 'bdtl': modeldtl_view_obj.bdtl,
                    'fingerprint': modeldtl_view_obj.fingerprint, 'back_flashlight': modeldtl_view_obj.back_flashlight,
                    'front_flashlight': modeldtl_view_obj.front_flashlight}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of Model',
                       'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    def update_BrandMaster(self, request):
        print('--', request.data)
        try:
            brand_view_obj = BrandMaster.objects.get(BrandID=request.data.get('BrandID'))
            brand_view_obj.BrandName = request.data.get('BrandName')
            brand_view_obj.save()

            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Brand Master Update'}

        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def get_UserByID(self, request):
        print('--', request.data)
        try:
            user_view_obj = UserMaster.objects.get(UserID=request.data.get('UserID'))
            data = {'UserID': user_view_obj.UserID, 'EmailID': user_view_obj.EmailID,
                    'FirstName': user_view_obj.FirstName, 'LastName': user_view_obj.LastName,
                    'isactive': user_view_obj.isactive}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of user',
                       'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data getuserbyid'}
        return Response(content)

    @action(methods=['POST'], detail=False)
    def get_DeviceByID(self, request):
        print('--', request.data)
        try:
            device_view_obj = DeviceMaster.objects.get(DeviceID=request.data.get('DeviceID'))
            data = {'DeviceID': device_view_obj.DeviceID, 'DeviceNumber': device_view_obj.DeviceNumber,
                    'DeviceAddress': device_view_obj.DeviceAddress, 'City': device_view_obj.City,
                    'State': device_view_obj.State, 'DeviceMac': device_view_obj.DeviceMac,
                    'isactive': device_view_obj.isactive}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of device',
                       'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data in getdevicebyid'}
        return Response(content)

    @action(methods=['POST'], detail=False)
    def get_DashbordData(self, request):
        print('--', request.data)
        try:
            device_view_obj = DeviceMaster.objects.filter(isactive=True).count()
            model_view_obj = ModelMaster.objects.filter(isactive=True).count()
            brand_view_ogject = BrandMaster.objects.filter().count()

            data = {'Brand_count': brand_view_ogject, 'Device_count': device_view_obj, 'Model_count': model_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of dashbord',
                       'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data in get_DashbordData'}

    def update_Model(self, request):
        print('--', request.data)
        try:
            header_dic = request.data.get('HeaderDic')
            dtl_dic = request.data.get('DtlDic')
            model_obj = ModelMaster.objects.get(header_dic.get('ModelID'))
            model_obj.ModelName = header_dic.get('ModelName')
            model_obj.BrandID = header_dic.get('BrandID')
            model_obj.save()

            model_dtl_obj = ModelDTL.objects.get(dtl_dic.get('ModelDTLID'))
            model_dtl_obj.RAM = dtl_dic.get('RAM')
            model_dtl_obj.Storage = dtl_dic.get('Storage')
            model_dtl_obj.price = dtl_dic.get('price')
            model_dtl_obj.back_camera1 = dtl_dic.get('back_camera1')
            model_dtl_obj.back_camera2 = dtl_dic.get('back_camera2')
            model_dtl_obj.back_camera3 = dtl_dic.get('back_camera3')
            model_dtl_obj.back_camera4 = dtl_dic.get('back_camera4')
            model_dtl_obj.back_camera5 = dtl_dic.get('back_camera5')
            model_dtl_obj.front_camara1 = dtl_dic.get('front_camara1')
            model_dtl_obj.front_camara2 = dtl_dic.get('front_camara2')
            model_dtl_obj.front_camara3 = dtl_dic.get('front_camara3')
            model_dtl_obj.front_camara4 = dtl_dic.get('front_camara4')
            model_dtl_obj.screen_size = dtl_dic.get('screen_size')
            model_dtl_obj.SIM_type = dtl_dic.get('expandable_storage')
            model_dtl_obj.color1 = dtl_dic.get('color1')
            model_dtl_obj.color2 = dtl_dic.get('color2')
            model_dtl_obj.color3 = dtl_dic.get('color3')
            model_dtl_obj.color4 = dtl_dic.get('color4')
            model_dtl_obj.color5 = dtl_dic.get('color5')
            model_dtl_obj.color6 = dtl_dic.get('color6')
            model_dtl_obj.color7 = dtl_dic.get('color7')
            model_dtl_obj.processor = dtl_dic.get('processor')
            model_dtl_obj.osdtl = dtl_dic.get('osdtl')
            model_dtl_obj.cpudtl = dtl_dic.get('cpudtl')
            model_dtl_obj.bdtl = dtl_dic.get('bdtl')
            model_dtl_obj.fingerprint = dtl_dic.get('fingerprint')
            model_dtl_obj.back_flashlight = dtl_dic.get('back_flashlight')
            model_dtl_obj.front_flashlight = dtl_dic.get('front_flashlight')
            model_dtl_obj.save()

            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Brand Master Update'}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def update_Device(self, request):
        print('--', request.data)
        try:
            device_obj = DeviceMaster.objects.get(DeviceID=request.data.get('DeviceID'))
            device_obj.DeviceNumber = request.data.get('DeviceNumber')
            device_obj.DeviceAddress = request.data.get('DeviceAddress')
            device_obj.City = request.data.get('City')
            device_obj.State = request.data.get('State')
            device_obj.DeviceMac = request.data('DeviceMac')
            device_obj.save()

            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Brand Master Update'}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def update_User(self, request):
        print('--', request.data)
        try:
            user_obj = UserMaster.objects.get(UserID=request.data.get('UserID'))
            user_obj.EmailID = request.data.get('EmailID')
            user_obj.FirstName = request.data.get('FirstName')
            user_obj.LastName = request.data.get('LastName')
            user_obj.save()
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Brand Master Update'}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)

    @action(methods=['POST'], details=False)
    def Login(self, request):
        print('--', request.data)
        try:
            login_obj = UserMaster.objects.get(EmailId=request.data.get('EmailID'),
                                               Password=request.data.get('Password'), IsActive=True)
            token = uuid.uuid4().hex
            ins_log = UserActiveLogon.objects.create(
                Token=token,
                UserID=login_obj.UserId

            )
            data = {'UserID': login_obj.UserId, 'EmailID': login_obj.EmailID, 'FirstName': login_obj.FirstName,
                    'LastName': login_obj.LastName,
                    'Password': login_obj.Password, 'IsActive': login_obj.IsActive, 'Token': token}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Login Success', 'data': data}

        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    @action(methods=['POST'], details=False)
    def Logout(self, request):
        print('--', request.data)
        try:
            ins_log = UserActiveLogon.objects.create(
                IsActive=False,
                UserID=request.data.get('UserID')
            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Logout Success'}

        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)
