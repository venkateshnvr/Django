# Generated by Django 3.0.4 on 2020-04-02 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200401_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersarray',
            name='activity_periods',
        ),
    ]
