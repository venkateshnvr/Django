# Generated by Django 3.0.4 on 2020-04-01 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_usersarray_tz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersarray',
            name='tz',
        ),
    ]
