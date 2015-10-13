# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='audio_filename',
            new_name='transcript',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='audio_filesize',
            new_name='video_filesize',
        ),
        migrations.AddField(
            model_name='video',
            name='video_filename',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='action',
            field=models.CharField(max_length=50, choices=[(b'convert', b'Convert'), (b'download', b'Download'), (b'transcribe', b'Transcribe')]),
        ),
    ]
