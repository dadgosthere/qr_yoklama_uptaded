# Generated by Django 5.0.3 on 2024-03-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_qrcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCodeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_code', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='QRCode',
        ),
    ]
