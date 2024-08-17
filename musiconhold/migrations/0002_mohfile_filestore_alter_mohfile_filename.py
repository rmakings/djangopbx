# Generated by Django 5.0.1 on 2024-08-10 13:32

import musiconhold.models
import pbx.commonwidgets
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiconhold', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mohfile',
            name='filestore',
            field=models.CharField(default='localhost', max_length=128, verbose_name='Filestore'),
        ),
        migrations.AlterField(
            model_name='mohfile',
            name='filename',
            field=pbx.commonwidgets.PbxFileField(storage=musiconhold.models.select_storage, upload_to=musiconhold.models.user_directory_path, verbose_name='File Name'),
        ),
    ]