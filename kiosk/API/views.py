from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Create your views here.

class Kiosk(ModelViewSet):
    queryset = BrandMaster.objects.all()
    serializer_class = BrandMasterSerializer

    # KIOSK
    @action(methods=['POST'], detail=False)
    def getmyid(self, request):
        print('--', request.data)
        try:
            device_obj = DeviceMaster.objecs.get(Devicemac=request.data.get('mac'))
            data = {'DeviceID': device_obj.DeviceID}
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'Here is your id', 'data': data}
        except Exception as e:
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
            content = {'result': 'Success', 'status': status.HTTP_200_OK, 'message': 'succesfully added',}
        except Exception as e:
            print(str(e))
            content = {'result': 'Fail', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                       'message': 'Error in fetching data'}
        return Response(content)
