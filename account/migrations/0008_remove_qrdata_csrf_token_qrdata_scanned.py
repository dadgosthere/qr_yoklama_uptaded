# Generated by Django 5.0.2 on 2024-05-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_qrdata_okul_numarasi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrdata',
            name='csrf_token',
        ),
        migrations.AddField(
            model_name='qrdata',
            name='scanned',
            field=models.BooleanField(default=False),
        ),
    ]
