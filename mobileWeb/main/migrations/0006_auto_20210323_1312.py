# Generated by Django 3.1.7 on 2021-03-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_socialaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaninfo',
            name='isAddiServ',
            field=models.BooleanField(null=True, verbose_name='살균,탈취'),
        ),
        migrations.AlterField(
            model_name='cleaninfo',
            name='isVideo',
            field=models.BooleanField(null=True, verbose_name='비디오 여부'),
        ),
    ]
