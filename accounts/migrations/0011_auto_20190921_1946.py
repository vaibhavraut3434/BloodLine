# Generated by Django 2.2.5 on 2019-09-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_organdonors_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing1',
            name='userid',
            field=models.CharField(default='x', max_length=12),
        ),
        migrations.AlterField(
            model_name='testing1',
            name='emergency',
            field=models.CharField(default='disagree', max_length=10),
        ),
    ]
