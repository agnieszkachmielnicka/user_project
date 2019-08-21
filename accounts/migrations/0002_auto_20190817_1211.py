# Generated by Django 2.2.4 on 2019-08-17 10:11

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='random_field',
            field=models.IntegerField(default=accounts.models.random_field),
        ),
    ]
