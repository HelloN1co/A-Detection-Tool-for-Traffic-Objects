# Generated by Django 2.1 on 2020-12-25 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201117_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='host',
            name='administrator',
        ),
        migrations.RemoveField(
            model_name='idc',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='groups',
        ),
    ]
