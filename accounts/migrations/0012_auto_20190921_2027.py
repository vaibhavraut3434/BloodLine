# Generated by Django 2.2.5 on 2019-09-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190921_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testing1',
            name='blood',
            field=models.CharField(default='O Positive', max_length=200),
        ),
        migrations.AlterField(
            model_name='testing1',
            name='city',
            field=models.CharField(default='some city   ', max_length=200),
        ),
        migrations.AlterField(
            model_name='testing1',
            name='country',
            field=models.CharField(default='some country', max_length=200),
        ),
        migrations.AlterField(
            model_name='testing1',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='testing1',
            name='state',
            field=models.CharField(default='some state', max_length=200),
        ),
        migrations.AlterField(
            model_name='testing1',
            name='userid',
            field=models.CharField(default='x', max_length=120),
        ),
    ]
