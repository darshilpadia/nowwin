from django.db import models

# Create your models here.

class BrandMaster(models.Model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=20)

    class Meta:
        db_table = 'BrandMaster'

class ModelMaster(models.Model):
    ModelID = models.AutoField(primary_key=True)
    ModelName = models.CharField(max_length=20)
    BrandID = models.ForeignKey('BrandMaster',on_delete=models.CASCADE)
    isactive = models.BooleanField(default=True)


    class Meta:
        db_table = 'ModelMaster'


class DeviceMaster(models.Model):
    DeviceID = models.AutoField(primary_key=True)
    DeviceNumber = models.CharField(max_length=20)
    DeviceAddress = models.CharField(max_length=250)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    DeviceMac = models.CharField(max_length=20)
    isactive =  models.BooleanField(default=True)

    class Meta:
        db_table = 'DeviceMaster'



class DeviceDTL(models.Model):
    DeviceDTLID = models.AutoField(primary_key=True)
    DeviceID = models.ForeignKey('DeviceMaster',on_delete=models.CASCADE)
    ModelID = models.ForeignKey('ModelMaster',on_delete=models.CASCADE)
    TotalScreenTime = models.CharField(max_length=6)
    CameraClick = models.IntegerField()
    RAMClick = models.IntegerField()
    StorageClick = models.IntegerField()
    OtherClick = models.IntegerField()

    class Meta:
        db_table = 'DeviceDTL'







