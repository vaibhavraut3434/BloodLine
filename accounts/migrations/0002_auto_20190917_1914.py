# Generated by Django 2.2.5 on 2019-09-17 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='img',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price',
        ),
    ]
