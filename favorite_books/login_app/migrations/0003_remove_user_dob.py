# Generated by Django 2.2 on 2020-06-11 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20200610_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='DOB',
        ),
    ]
