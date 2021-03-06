# Generated by Django 3.0.3 on 2020-02-25 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandMaster',
            fields=[
                ('BrandID', models.AutoField(primary_key=True, serialize=False)),
                ('BrandName', models.CharField(max_length=20)),
                ('isactive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'BrandMaster',
            },
        ),
        migrations.CreateModel(
            name='DeviceDTL',
            fields=[
                ('DeviceDTLID', models.AutoField(primary_key=True, serialize=False)),
                ('TotalScreenTime', models.CharField(max_length=6)),
                ('Front_CameraClick', models.IntegerField(blank=True, null=True)),
                ('Back_CameraClick', models.IntegerField(blank=True, null=True)),
                ('ScreenSizeClick', models.IntegerField(blank=True, null=True)),
                ('ColorClick', models.IntegerField(blank=True, null=True)),
                ('RAMClick', models.IntegerField(blank=True, null=True)),
                ('StorageClick', models.IntegerField(blank=True, null=True)),
                ('OtherClick', models.IntegerField(blank=True, null=True)),
                ('InterActionDateTime', models.DateTimeField(default='2020-02-25 16:35:29')),
            ],
            options={
                'db_table': 'DeviceDTL',
            },
        ),
        migrations.CreateModel(
            name='DeviceMaster',
            fields=[
                ('DeviceID', models.AutoField(primary_key=True, serialize=False)),
                ('DeviceNumber', models.CharField(max_length=20)),
                ('DeviceAddress', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('DeviceMac', models.CharField(max_length=20)),
                ('isactive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'DeviceMaster',
            },
        ),
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('EmailID', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=255)),
                ('IsActive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'UserMaster',
            },
        ),
        migrations.CreateModel(
            name='UserActiveLogon',
            fields=[
                ('ActiveLogonID', models.AutoField(primary_key=True, serialize=False)),
                ('Token', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.UserMaster')),
            ],
            options={
                'db_table': 'UserActiveLogon',
            },
        ),
        migrations.CreateModel(
            name='ModelMaster',
            fields=[
                ('ModelID', models.AutoField(primary_key=True, serialize=False)),
                ('ModelName', models.CharField(max_length=20)),
                ('isactive', models.BooleanField(default=True)),
                ('BrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.BrandMaster')),
            ],
            options={
                'db_table': 'ModelMaster',
            },
        ),
        migrations.CreateModel(
            name='ModelDTL',
            fields=[
                ('ModelDTLID', models.AutoField(primary_key=True, serialize=False)),
                ('RAM', models.CharField(max_length=2)),
                ('Storage', models.CharField(max_length=6)),
                ('price', models.CharField(max_length=10)),
                ('back_camera1', models.CharField(blank=True, max_length=20, null=True)),
                ('back_camera2', models.CharField(blank=True, max_length=20, null=True)),
                ('back_camera3', models.CharField(blank=True, max_length=20, null=True)),
                ('back_camera4', models.CharField(blank=True, max_length=20, null=True)),
                ('back_camera5', models.CharField(blank=True, max_length=20, null=True)),
                ('front_camara1', models.CharField(blank=True, max_length=20, null=True)),
                ('front_camara2', models.CharField(blank=True, max_length=20, null=True)),
                ('front_camara3', models.CharField(blank=True, max_length=20, null=True)),
                ('front_camara4', models.CharField(blank=True, max_length=20, null=True)),
                ('screen_size', models.CharField(max_length=10)),
                ('SIM_type', models.CharField(max_length=10)),
                ('expandable_storage', models.CharField(max_length=10)),
                ('color1', models.CharField(blank=True, max_length=10, null=True)),
                ('color2', models.CharField(blank=True, max_length=10, null=True)),
                ('color3', models.CharField(blank=True, max_length=10, null=True)),
                ('color4', models.CharField(blank=True, max_length=10, null=True)),
                ('color5', models.CharField(blank=True, max_length=10, null=True)),
                ('color6', models.CharField(blank=True, max_length=10, null=True)),
                ('color7', models.CharField(blank=True, max_length=10, null=True)),
                ('processor', models.CharField(max_length=50)),
                ('osdtl', models.CharField(max_length=30)),
                ('cpudtl', models.CharField(max_length=30)),
                ('bdtl', models.CharField(max_length=30)),
                ('fingerprint', models.CharField(max_length=50)),
                ('back_flashlight', models.BooleanField()),
                ('front_flashlight', models.BooleanField()),
                ('ModelID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.ModelMaster')),
            ],
            options={
                'db_table': 'ModelDTL',
            },
        ),
        migrations.CreateModel(
            name='KioskActiveLogon',
            fields=[
                ('KioskLogonID', models.AutoField(primary_key=True, serialize=False)),
                ('Token', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField()),
                ('DeviceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.DeviceDTL')),
            ],
            options={
                'db_table': 'KioskActiveLogon',
            },
        ),
        migrations.AddField(
            model_name='devicedtl',
            name='DeviceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.DeviceMaster'),
        ),
        migrations.AddField(
            model_name='devicedtl',
            name='ModelID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.ModelMaster'),
        ),
    ]
