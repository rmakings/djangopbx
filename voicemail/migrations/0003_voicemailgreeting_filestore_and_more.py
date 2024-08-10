# Generated by Django 5.0.1 on 2024-08-10 13:31

import pbx.commonwidgets
import voicemail.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voicemail', '0002_alter_voicemail_alternate_greeting_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voicemailgreeting',
            name='filestore',
            field=models.CharField(default='localhost', max_length=128, verbose_name='Filestore'),
        ),
        migrations.AlterField(
            model_name='voicemailgreeting',
            name='filename',
            field=pbx.commonwidgets.PbxFileField(storage=voicemail.models.select_storage, upload_to=voicemail.models.user_directory_path, verbose_name='File Name'),
        ),
    ]
