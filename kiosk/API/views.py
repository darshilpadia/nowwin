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
    def get_BrandView(self,request):
        print('--', request.data)
        try:
            brand_view_obj= BrandMaster.objects.filter()
            data={'brand_list', brand_view_obj}
            content= {'result':'Success','status': status.HTTP_200_OK,'message':'List of Brand','data':data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Error in fetching data'}

        return Response(content)

    @action(method=['POST'], detail=False)
    def get_ModelView(self, request):
        print('--', request.data)
        try:
            model_view_obj = ModelMaster.ojects.filter(isactive=True)
            data={'model_list', model_view_obj}
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
            data={'user_list', user_view_obj}
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
            device_view_obj= DeviceMaster.objects.filter(isactive=True)
            data={'device_list',device_view_obj}
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

    @action(methods=['POST'], details=False)
    def Login(self, request):
        print('--',request.data)
        try:
            login_obj= UserMaster.objects.get(EmailId=request.data.get('EmailID'),Password=request.data.get('Password'),IsActive=True)
            token=uuid.uuid4().hex
            ins_log = UserActiveLogon.objects.create(
                Token=token,
                UserID=login_obj.UserId

            )
            data= {'UserID':login_obj.UserId, 'EmailID':login_obj.EmailID,'FirstName':login_obj.FirstName,'LastName':login_obj.LastName
                   'Password':login_obj.Password,'IsActive' : login_obj.IsActive,'Token':token}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Login Success', 'data': data}

        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

    @action(methods=['POST'], details=False)
    def Logout(self,request):
        print('--',request.data)
        try:
            ins_log=UserActiveLogon.objects.create(
                IsActive = False,
                UserID=request.data.get('UserID')
            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Logout Success'}

        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                   'message': 'Error in fetching data'}

        return Response(content)
