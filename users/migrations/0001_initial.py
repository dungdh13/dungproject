# Generated by Django 3.0.4 on 2020-03-31 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sot', models.BooleanField(default=False)),
                ('nhiet_do', models.FloatField(default=37, null=True)),
                ('ho', models.BooleanField(default=False)),
                ('dau_hong', models.BooleanField(default=False)),
                ('met_moi', models.BooleanField(default=False)),
                ('dau_dau', models.BooleanField(default=False)),
                ('ret_run', models.BooleanField(default=False)),
                ('dau_co', models.BooleanField(default=False)),
                ('non', models.BooleanField(default=False)),
                ('buon_non', models.BooleanField(default=False)),
                ('kho_tho', models.BooleanField(default=False)),
                ('tiepxuc_f0', models.BooleanField(default=False)),
                ('tiepxuc_f1', models.BooleanField(default=False)),

                ('vung_dich', models.BooleanField(default=False)),
                ('tt_banthan', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Thông tin sức khỏe',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_chi', models.CharField(blank=True, max_length=60)),
                ('khoa_phong', models.CharField(blank=True, max_length=40)),
                ('Ho_ten', models.CharField(blank=True, max_length=40)),
                ('sdt', models.BigIntegerField(blank=True, null=True)),
                ('MSBN', models.BigIntegerField(blank=True, null=True)),
                ('cd_benh', models.CharField(blank=True, max_length=120)),
                ('lich_hen_kham', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Thông tin cá nhân',
            },
        ),
    ]
