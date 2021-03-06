# Generated by Django 3.1.7 on 2021-03-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210309_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='종류')),
                ('key', models.CharField(max_length=300, verbose_name='키 값')),
                ('secret_key', models.CharField(max_length=300, null=True, verbose_name='secret key')),
            ],
            options={
                'verbose_name': '소셜 계정 관리',
                'verbose_name_plural': '소셜 계정 관리',
                'db_table': 'social_account',
            },
        ),
    ]
