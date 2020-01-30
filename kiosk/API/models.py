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





