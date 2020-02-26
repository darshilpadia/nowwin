from django.shortcuts import render
import uuid
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from collections import Counter
from datetime import datetime


# Create your views here.


def validate_user(func):
    def inner(**kwargs):
        print('called')
        u = Utils()
        # u.VerifyUser()
        return func

    return inner


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


# class ModelAPIView(ModelViewSet):
#     queryset = ModelMaster.objects.all()
#     serializer_class = ModelMasterSerializer
#
#     @action(methods=['POST'], detail=False)
#     def get_ModelView(self, request):
#         print('--', request.data)
#         try:
#             model_view_obj = ModelMaster.objects.filter(isactive=True)
#             data = {'model_list', model_view_obj}
#             content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Model', 'data': data}
#         except Exception as e:
#             print(str(e))
#             content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                        'message': 'Error in fetching data'}
#
#         return Response(content)


class Kiosk(ModelViewSet):
    queryset = DeviceMaster.objects.all()
    serializer_class = BrandMasterSerializer

    # queryset1 = ModelMaster.objects.all()
    # serializer_class1 = ModelMasterSerializer
    # KIOSK
    @action(methods=['POST'], detail=False)
    def getmyid(self, request):
        print('--', request.data)
        try:
            device_obj = DeviceMaster.objects.get(DeviceMac=request.data.get('mac'))
            data = {'DeviceID': device_obj.DeviceID}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Here is your id', 'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

        # KIOSK

    @action(methods=['GET'], detail=False)
    def getmyid1(self, request):
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
                DeviceNumber=request.data.get('DeviceNumber'),
                DeviceAddress=request.data.get('DeviceAddress'),
                City=request.data.get('City'),
                State=request.data.get('State'),
                DeviceMac=request.data.get('DeviceMac'),

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
        print('--', type(request.data))
        try:
            ins_obj = DeviceDTL.objects.create(
                DeviceID_id=request.data.get('deviceid'),
                ModelID_id=request.data.get('modelid'),
                TotalScreenTime=request.data.get('total_screen_time'),
                Front_CameraClick=request.data.get('front_camera_click'),
                Back_CameraClick=request.data.get('back_camera_click'),
                ScreenSizeClick=request.data.get('screen_size_click'),
                ColorClick=request.data.get('color_click'),
                RAMClick=request.data.get('ram_click'),
                StorageClick=request.data.get('storage_click'),
                OtherClick=request.data.get('other_click')  # ,
                # InterActionDateTime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added', }
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

        # ADMIN SIDE

    @action(methods=['POST'], detail=False)
    def ins_ModelDTL(self, request):
        print('--', request.data)
        try:
            ins_obj = ModelDTL.objects.create(
                ModelID_id=request.data.get('ModelID'),
                RAM=request.data.get('ram'),
                Storage=request.data.get('storage'),
                price=request.data.get('price'),
                back_camera1=request.data.get('back_camera1'),
                back_camera2=request.data.get('back_camera2'),
                back_camera3=request.data.get('back_camera3'),
                back_camera4=request.data.get('back_camera4'),
                back_camera5=request.data.get('back_camera5'),
                front_camara1=request.data.get('front_camara1'),
                front_camara2=request.data.get('front_camara2'),
                front_camara3=request.data.get('front_camara3'),
                front_camara4=request.data.get('front_camara4'),
                screen_size=request.data.get('screen_size'),
                SIM_type=request.data.get('sim_type'),
                expandable_storage=request.data.get('expandable_storage'),
                color1=request.data.get('color1'),
                color2=request.data.get('color2'),
                color3=request.data.get('color3'),
                color4=request.data.get('color4'),
                color5=request.data.get('color5'),
                color6=request.data.get('color6'),
                color7=request.data.get('color7'),
                processor=request.data.get('processor'),
                osdtl=request.data.get('osdtl'),
                cpudtl=request.data.get('cpudtl'),
                bdtl=request.data.get('bdtl'),
                fingerprint=request.data.get('fingerprint'),
                back_flashlight=request.data.get('back_flashlight'),
                front_flashlight=request.data.get('front_flashlight')

            )
            print('update puru')
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
                BrandName=request.data.get('BrandName')
            )
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added', }
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)

        # ADMIN SIDE

    @action(methods=['POST'], detail=False)
    def ins_ModelMaster(self, request):
        print('--', request.data)
        try:

            ins_obj = ModelMaster.objects.create(
                ModelName=request.data.get('modelname'),
                BrandID_id=request.data.get('brandid')

            )
            print('insert done')
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added',
                       'ModelID': ins_obj.ModelID
                       }
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

    @action(methods=['POST'], detail=False)
    def get_BrandView(self, request):
        print('**************************************call bc')
        try:

            brand_view_obj = BrandMaster.objects.filter()
            print(brand_view_obj)
            try:
                if request.data.get('flag'):
                    datalist = []
                    for x in brand_view_obj:
                        datalist.append({'brandname': x.BrandName})
                    data = {'brand_list': datalist}
                    content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Brand',
                               'data': data}

                else:

                    content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Brand',
                               'data': brand_view_obj}
            except AttributeError as c:
                content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Brand',
                           'data': brand_view_obj}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)

    @action(methods=['POST'], detail=False)
    def get_ModelView(self, request):
        # print('--', request.data)
        try:
            model_view_obj = ModelMaster.objects.filter(isactive=True)
            try:
                if request.data.get('flag'):
                    datalist = []
                    for x in model_view_obj:
                        datalist.append({'modelname': x.ModelName, 'modelid': x.ModelID})
                    data = {'brand_list': datalist}
                    content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Brand',
                               'data': data}
                else:

                    content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Model',
                               'data': model_view_obj}
            except AttributeError as cc:
                datalist = []
                for x in model_view_obj:
                    brandname = BrandMaster.objects.get(BrandID=x.BrandID_id)
                    datalist.append({'ModelName': x.ModelName, 'ModelID': x.ModelID, 'BrandName': brandname.BrandName})
                # data = {'brand_list': datalist}
                content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of Brand',
                           'data': datalist}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}

        return Response(content)

    # @action(methods=['POST'], detail=False)
    # def get_ModelView(self, request):
    #     # print('--', request.data)
    #     try:
    #         model_view_obj = ModelMaster.objects.filter(isactive=True)
    #
    #         modeldtl_view_obj = ModelDTL.objects.get(ModelID_id=model_view_obj.ModelID)
    #
    #         data = {'ModelID': model_view_obj.ModelID, 'ModelName': model_view_obj.ModelName,
    #                 'BrandID': model_view_obj.BrandID, 'isactive': model_view_obj.isactive,
    #                 'ModelDTLID': modeldtl_view_obj.ModelDTLID, 'RAM': modeldtl_view_obj.RAM,
    #                 'Storage': modeldtl_view_obj.Storage, 'price': modeldtl_view_obj.price,
    #                 'back_camera1': modeldtl_view_obj.back_camera1, 'back_camera2': modeldtl_view_obj.back_camera2,
    #                 'back_camera3': modeldtl_view_obj.back_camera3, 'back_camera4': modeldtl_view_obj.back_camera4,
    #                 'back_camera5': modeldtl_view_obj.back_camera5, 'front_camara1': modeldtl_view_obj.front_camara1,
    #                 'front_camara2': modeldtl_view_obj.front_camara2, 'front_camara3': modeldtl_view_obj.front_camara3,
    #                 'front_camara4': modeldtl_view_obj.front_camara4, 'screen_size': modeldtl_view_obj.screen_size,
    #                 'SIM_type': modeldtl_view_obj.SIM_type, 'expandable_storage': modeldtl_view_obj.expandable_storage,
    #                 'color1': modeldtl_view_obj.color1, 'color2': modeldtl_view_obj.color2,
    #                 'color3': modeldtl_view_obj.color3, 'color4': modeldtl_view_obj.color4,
    #                 'color5': modeldtl_view_obj.color5, 'color6': modeldtl_view_obj.color6,
    #                 'color7': modeldtl_view_obj.color7, 'processor': modeldtl_view_obj.processor,
    #                 'osdtl': modeldtl_view_obj.osdtl, 'bdtl': modeldtl_view_obj.bdtl,
    #                 'fingerprint': modeldtl_view_obj.fingerprint, 'back_flashlight': modeldtl_view_obj.back_flashlight,
    #                 'front_flashlight': modeldtl_view_obj.front_flashlight}
    #
    #         content = {'result': 'Success', 'data': data}
    #
    #     except Exception as e:
    #         print(str(e))
    #         content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                    'message': 'Error in fetching data'}
    #
    #     return Response(content)

    @action(methods=['POST'], detail=False)
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

    # @action(methods=['POST'], detail=False)
    # def get_ModelID_By_DeviceID(self, request):
    #     print('--', request.data)
    #     try:
    #         user_view_obj = Mo.objects.filter(DeviceID=request.data.get('DeviceID'))
    #         data = {'user_list', user_view_obj}
    #         print(data)
    #         content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of User', 'data': data}
    #     except Exception as e:
    #         print(str(e))
    #         content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                    'message': 'Error in fetching data'}
    #
    #     return Response(content)

    @action(methods=['POST'], detail=False)
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

    @action(methods=['POST'], detail=False)
    def get_DeviceView(self, request):
        # print('--', request.data)
        try:
            device_view_obj = DeviceMaster.objects.filter(isactive=True)
            data = {'device_list', device_view_obj}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'List of device',
                       'data': device_view_obj}
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
    def get_ModelDtl4Kiosk(self, request):
        print('--', request.data)
        try:
            datalist = []
            model_view_obj = ModelMaster.objects.filter(isactive=True)
            for x in model_view_obj:
                print(x.ModelID)
                modeldtl_view_obj = ModelDTL.objects.get(ModelID_id=x.ModelID)
                data = {'ModelID': x.ModelID, 'ModelName': x.ModelName,
                        'isactive': x.isactive,
                        'ModelDTLID': modeldtl_view_obj.ModelDTLID, 'RAM': modeldtl_view_obj.RAM,
                        'Storage': modeldtl_view_obj.Storage, 'price': modeldtl_view_obj.price,
                        'back_camera1': modeldtl_view_obj.back_camera1, 'back_camera2': modeldtl_view_obj.back_camera2,
                        'back_camera3': modeldtl_view_obj.back_camera3, 'back_camera4': modeldtl_view_obj.back_camera4,
                        'back_camera5': modeldtl_view_obj.back_camera5,
                        'front_camera1': modeldtl_view_obj.front_camara1,
                        'front_camera2': modeldtl_view_obj.front_camara2,
                        'front_camera3': modeldtl_view_obj.front_camara3,
                        'front_camera4': modeldtl_view_obj.front_camara4, 'screen_size': modeldtl_view_obj.screen_size,
                        'sim_type': modeldtl_view_obj.SIM_type,
                        'expandable_storage': modeldtl_view_obj.expandable_storage,
                        'color1': modeldtl_view_obj.color1, 'color2': modeldtl_view_obj.color2,
                        'color3': modeldtl_view_obj.color3, 'color4': modeldtl_view_obj.color4,
                        'color5': modeldtl_view_obj.color5, 'color6': modeldtl_view_obj.color6,
                        'color7': modeldtl_view_obj.color7, 'processor': modeldtl_view_obj.processor,
                        'os_details': modeldtl_view_obj.osdtl, 'battery_details': modeldtl_view_obj.bdtl,
                        'fingerprint': modeldtl_view_obj.fingerprint,
                        'back_flashlight': modeldtl_view_obj.back_flashlight,
                        'front_flashlight': modeldtl_view_obj.front_flashlight, 'cpu_details': modeldtl_view_obj.cpudtl}
                bc_list = ['back_camera1', 'back_camera2', 'back_camera3', 'back_camera4', 'back_camera5']
                fc_list = ['front_camera1', 'front_camera2', 'front_camera3', 'front_camera4']
                bc_count = 0
                fc_count = 0
                for x in bc_list:
                    if data.get(x) is not None:
                        bc_count += 1

                for x in fc_list:
                    if data.get(x) is not None:
                        fc_count += 1

                data['bc_count'] = bc_count
                data['fc_count'] = fc_count
                # bc_camera_list = []

                datalist.append(data)
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of Model',
                       'data': datalist}
            print(content)
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
            modeldtl_view_obj = ModelDTL.objects.get(ModelID_id=request.data.get('ModelID'))
            data = {'ModelID': model_view_obj.ModelID, 'ModelName': model_view_obj.ModelName,
                    'BrandID': model_view_obj.BrandID, 'isactive': model_view_obj.isactive,
                    'ModelDTLID': modeldtl_view_obj.ModelDTLID, 'RAM': modeldtl_view_obj.RAM,
                    'Storage': modeldtl_view_obj.Storage, 'price': modeldtl_view_obj.price,
                    'back_camera1': modeldtl_view_obj.back_camera1, 'back_camera2': modeldtl_view_obj.back_camera2,
                    'back_camera3': modeldtl_view_obj.back_camera3, 'back_camera4': modeldtl_view_obj.back_camera4,
                    'back_camera5': modeldtl_view_obj.back_camera5, 'front_camera1': modeldtl_view_obj.front_camara1,
                    'front_camera2': modeldtl_view_obj.front_camara2, 'front_camera3': modeldtl_view_obj.front_camara3,
                    'front_camera4': modeldtl_view_obj.front_camara4, 'screen_size': modeldtl_view_obj.screen_size,
                    'sim_type': modeldtl_view_obj.SIM_type, 'expandable_storage': modeldtl_view_obj.expandable_storage,
                    'color1': modeldtl_view_obj.color1, 'color2': modeldtl_view_obj.color2,
                    'color3': modeldtl_view_obj.color3, 'color4': modeldtl_view_obj.color4,
                    'color5': modeldtl_view_obj.color5, 'color6': modeldtl_view_obj.color6,
                    'color7': modeldtl_view_obj.color7, 'processor': modeldtl_view_obj.processor,
                    'os_details': modeldtl_view_obj.osdtl, 'battery_details': modeldtl_view_obj.bdtl,
                    'fingerprint': modeldtl_view_obj.fingerprint, 'back_flashlight': modeldtl_view_obj.back_flashlight,
                    'front_flashlight': modeldtl_view_obj.front_flashlight, 'cpu_details': modeldtl_view_obj.cpudtl}
            bc_list = ['back_camera1', 'back_camera2', 'back_camera3', 'back_camera4', 'back_camera5']
            fc_list = ['front_camera1', 'front_camera2', 'front_camera3', 'front_camera4']
            bc_count = 0
            fc_count = 0
            for x in bc_list:
                if data.get(x) is not None:
                    bc_count += 1

            for x in fc_list:
                if data.get(x) is not None:
                    fc_count += 1

            data['bc_count'] = bc_count
            data['fc_count'] = fc_count

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
    # @validate_user
    def get_DashbordData(self, request):
        # print('--', request.data)
        try:
            device_view_obj = DeviceMaster.objects.filter(isactive=True).count()
            model_view_obj = ModelMaster.objects.filter(isactive=True).count()
            brand_view_ogject = BrandMaster.objects.filter().count()
            devicedtl_view_obj = DeviceDTL.objects.filter().count()
            dashboard_chart_obj = SPM0dels.get_dashboard_chartdata()
            print(dashboard_chart_obj)
            chart_count_list = []
            chart_label_list = []
            chart_model_list = []

            for x in dashboard_chart_obj:
                chart_count_list.append(x[0])
                chart_label_list.append(x[1])
                chart_model_list.append(x[2])

            temp = Counter(chart_model_list)
            pie_chart_lable = []
            pie_chart_count = []
            print(temp)
            for a, b in temp.items():
                pie_chart_count.append(b)
                pie_chart_lable.append(a)
            if len(chart_count_list) > 0:
                best = max(chart_count_list)
                avg = sum(chart_count_list) / len(chart_count_list)
                this_week = sum(chart_count_list)
            else:
                best =None
                avg = None
                this_week = None

            data = {'Brand_count': brand_view_ogject, 'Device_count': device_view_obj, 'Model_count': model_view_obj,
                    'DeviceDTL_count': devicedtl_view_obj, 'Count_list': chart_count_list,
                    'Label_list': chart_label_list,
                    'Model_list': chart_model_list,
                    'best':  best,
                    'avg': avg,
                    'this_week':  this_week,
                    'pie_label_list': pie_chart_lable, 'pie_count_list': pie_chart_count}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Detail Of dashbord',
                       'data': data}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data in get_DashbordData'}
        return Response(content)

    def update_Model(self, request):
        print('--', request.data)
        try:

            model_obj = ModelMaster.objects.get(request.data.get('ModelID'))
            model_obj.ModelName = request.data.get('modelname')
            model_obj.BrandID = request.data.get('brandid')
            model_obj.save()

            model_dtl_obj = ModelDTL.objects.get(request.data.get('ModelDTLID'))
            model_dtl_obj.RAM = request.data.get('RAM')
            model_dtl_obj.Storage = request.data.get('Storage')
            model_dtl_obj.price = request.data.get('price')
            model_dtl_obj.back_camera1 = request.data.get('back_camera1')
            model_dtl_obj.back_camera2 = request.data.get('back_camera2')
            model_dtl_obj.back_camera3 = request.data.get('back_camera3')
            model_dtl_obj.back_camera4 = request.data.get('back_camera4')
            model_dtl_obj.back_camera5 = request.data.get('back_camera5')
            model_dtl_obj.front_camara1 = request.data.get('front_camara1')
            model_dtl_obj.front_camara2 = request.data.get('front_camara2')
            model_dtl_obj.front_camara3 = request.data.get('front_camara3')
            model_dtl_obj.front_camara4 = request.data.get('front_camara4')
            model_dtl_obj.screen_size = request.data.get('screen_size')
            model_dtl_obj.SIM_type = request.data.get('expandable_storage')
            model_dtl_obj.color1 = request.data.get('color1')
            model_dtl_obj.color2 = request.data.get('color2')
            model_dtl_obj.color3 = request.data.get('color3')
            model_dtl_obj.color4 = request.data.get('color4')
            model_dtl_obj.color5 = request.data.get('color5')
            model_dtl_obj.color6 = request.data.get('color6')
            model_dtl_obj.color7 = request.data.get('color7')
            model_dtl_obj.processor = request.data.get('processor')
            model_dtl_obj.osdtl = request.data.get('osdtl')
            model_dtl_obj.cpudtl = request.data.get('cpudtl')
            model_dtl_obj.bdtl = request.data.get('bdtl')
            model_dtl_obj.fingerprint = request.data.get('fingerprint')
            model_dtl_obj.back_flashlight = request.data.get('back_flashlight')
            model_dtl_obj.front_flashlight = request.data.get('front_flashlight')
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
            device_obj.DeviceMac = request.data.get('DeviceMac')
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

    @action(methods=['POST'], detail=False)
    def Login(self, request):
        print('--', request)
        print('--', request.data)
        try:
            login_obj = UserMaster.objects.get(EmailID=request.data.get('EmailID'),
                                               Password=request.data.get('Password'), IsActive=True)
            token = uuid.uuid4().hex
            ins_log = UserActiveLogon.objects.create(
                Token=token,
                UserID_id=login_obj.UserID

            )
            data = {'UserID': login_obj.UserID, 'EmailID': login_obj.EmailID, 'FirstName': login_obj.FirstName,
                    'LastName': login_obj.LastName,
                    'Password': login_obj.Password, 'IsActive': login_obj.IsActive, 'Token': token}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Login Success', 'data': data}

        except UserMaster.DoesNotExist as e:

            content = {'result': 'Forbidden', 'status': status.HTTP_200_OK, 'message': 'No user'}

        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        print(content)
        return Response(content)

    @action(methods=['POST'], detail=False)
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

    # ADMIN SIDE
    @action(methods=['POST'], detail=False)
    def del_ModelMaster(self, request):
        print('--', request.data)
        try:
            model_obj = ModelMaster.objects.get(ModelID=request.data.get('ModelID'))
            model_obj.isactive = False
            model_obj.save()
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully deleted', }
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)
