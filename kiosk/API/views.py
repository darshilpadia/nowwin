from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Create your views here.

class Kiosk(ModelViewSet):
    queryset = BrandMaster.objects.all()
    serializer_class = BrandMasterSerializer

    @action(methods=['POST'], detail=False)
    def getmyid(self, request):
        print('--', request.data)
