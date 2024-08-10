# Generated by Django 5.0.1 on 2024-08-10 16:04

import tenants.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0007_populate_portal_name_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='portal_name',
            field=models.CharField(db_index=True, default=tenants.models.default_portal, help_text='Eg. tenant1.pbxportal.com', max_length=128, unique=True, verbose_name='Portal Name'),
        ),
    ]
