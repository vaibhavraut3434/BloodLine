# Generated by Django 2.2.5 on 2019-09-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0012_auto_20190919_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostcamp',
            name='image',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
