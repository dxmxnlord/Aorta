# Generated by Django 2.2.5 on 2019-09-14 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190914_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='profilepicture',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='profilepicture',
        ),
    ]
