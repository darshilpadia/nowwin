from django.db import models, connection
from datetime import datetime


# Create your models here.

class SPM0dels():

    @staticmethod
    def get_dashboard_chartdata():
        cur = connection.cursor()
        cur.callproc('get_dashboard_chart_data')
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def get_general_report():
        cur = connection.cursor()
        cur.callproc('get_general_report')
        result = cur.fetchall()
        cur.close()
        return result


class BrandMaster(models.Model):
    BrandID = models.AutoField(primary_key=True)
    BrandName = models.CharField(max_length=20)
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'BrandMaster'


class ModelMaster(models.Model):
    ModelID = models.AutoField(primary_key=True)
    ModelName = models.CharField(max_length=20)
    BrandID = models.ForeignKey('BrandMaster', on_delete=models.CASCADE)
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
    isactive = models.BooleanField(default=True)

    class Meta:
        db_table = 'DeviceMaster'


class DeviceDTL(models.Model):
    DeviceDTLID = models.AutoField(primary_key=True)
    DeviceID = models.ForeignKey('DeviceMaster', on_delete=models.CASCADE)
    ModelID = models.ForeignKey('ModelMaster', on_delete=models.CASCADE)
    TotalScreenTime = models.CharField(max_length=6)
    Front_CameraClick = models.IntegerField(null=True, blank=True)
    Back_CameraClick = models.IntegerField(null=True, blank=True)
    ScreenSizeClick = models.IntegerField(null=True, blank=True)
    ColorClick = models.IntegerField(null=True, blank=True)
    RAMClick = models.IntegerField(null=True, blank=True)
    StorageClick = models.IntegerField(null=True, blank=True)
    OtherClick = models.IntegerField(null=True, blank=True)
    InterActionDateTime = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        db_table = 'DeviceDTL'


class UserMaster(models.Model):
    UserID = models.AutoField(primary_key=True)
    EmailID = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=15)
    Password = models.CharField(max_length=255)
    IsActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'UserMaster'


class UserActiveLogon(models.Model):
    ActiveLogonID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey('UserMaster', on_delete=models.CASCADE)
    Token = models.CharField(max_length=50)
    IsActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'UserActiveLogon'


class KioskActiveLogon(models.Model):
    KioskLogonID = models.AutoField(primary_key=True)
    DeviceID = models.ForeignKey('DeviceDTL', on_delete=models.CASCADE)
    Token = models.CharField(max_length=50)
    IsActive = models.BooleanField()

    class Meta:
        db_table = 'KioskActiveLogon'


class ModelDTL(models.Model):
    ModelDTLID = models.AutoField(primary_key=True)
    ModelID = models.ForeignKey('ModelMaster', on_delete=models.CASCADE)
    RAM = models.CharField(max_length=2)
    Storage = models.CharField(max_length=6)
    price = models.CharField(max_length=10)
    back_camera1 = models.CharField(max_length=20, null=True, blank=True)
    back_camera2 = models.CharField(max_length=20, null=True, blank=True)
    back_camera3 = models.CharField(max_length=20, null=True, blank=True)
    back_camera4 = models.CharField(max_length=20, null=True, blank=True)
    back_camera5 = models.CharField(max_length=20, null=True, blank=True)
    front_camara1 = models.CharField(max_length=20, null=True, blank=True)
    front_camara2 = models.CharField(max_length=20, null=True, blank=True)
    front_camara3 = models.CharField(max_length=20, null=True, blank=True)
    front_camara4 = models.CharField(max_length=20, null=True, blank=True)
    screen_size = models.CharField(max_length=10)
    SIM_type = models.CharField(max_length=10)
    expandable_storage = models.CharField(max_length=10)
    color1 = models.CharField(max_length=10, null=True, blank=True)
    color2 = models.CharField(max_length=10, null=True, blank=True)
    color3 = models.CharField(max_length=10, null=True, blank=True)
    color4 = models.CharField(max_length=10, null=True, blank=True)
    color5 = models.CharField(max_length=10, null=True, blank=True)
    color6 = models.CharField(max_length=10, null=True, blank=True)
    color7 = models.CharField(max_length=10, null=True, blank=True)
    processor = models.CharField(max_length=50)
    osdtl = models.CharField(max_length=30)
    cpudtl = models.CharField(max_length=30)
    bdtl = models.CharField(max_length=30)
    fingerprint = models.CharField(max_length=50)
    back_flashlight = models.BooleanField()
    front_flashlight = models.BooleanField()

    class Meta:
        db_table = 'ModelDTL'
