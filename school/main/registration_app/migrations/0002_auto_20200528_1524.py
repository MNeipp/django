# Generated by Django 2.2 on 2020-05-28 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='all_students',
            field=models.ManyToManyField(related_name='subjects', to='registration_app.Student'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='all_teachers',
            field=models.ManyToManyField(related_name='subjects', to='registration_app.Teacher'),
        ),
    ]