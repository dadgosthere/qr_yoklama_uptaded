# Generated by Django 5.0.2 on 2024-05-29 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_rename_qrdata2_qrdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCodeData2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('akademisyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.akademisyen')),
            ],
        ),
        migrations.CreateModel(
            name='QRData2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_data', models.CharField(max_length=255)),
                ('csrf_token', models.CharField(max_length=255)),
                ('okul_numarasi', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('akademisyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.akademisyen')),
            ],
        ),
        migrations.DeleteModel(
            name='QRCodeData',
        ),
        migrations.DeleteModel(
            name='QRData',
        ),
    ]