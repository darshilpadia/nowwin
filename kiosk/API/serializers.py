from rest_framework import serializers
from .models import *


class BrandMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandMaster
        feilds = '__all__'