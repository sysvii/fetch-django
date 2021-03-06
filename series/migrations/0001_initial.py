# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 21:36
from __future__ import unicode_literals

import app.storage
import app.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import series.util


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the media type', max_length=80)),
                ('available_options', jsonfield.fields.JSONField(default='{\n    "properties":\n    {\n        "id": {\n            "title": "ID",\n            "type": "integer"\n            }\n    },\n    "required": ["id"]\n}', help_text='A JSON schema of options that the media type allows', validators=[app.validators.json_schema_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Name of the series')),
                ('search_title', models.CharField(blank=True, default='', max_length=256, verbose_name='String to be used when searching for the series')),
                ('save_path', models.CharField(blank=True, default='', max_length=256, verbose_name='Path to be sorted into')),
                ('info_url', models.URLField(blank=True, verbose_name='Information URL')),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('release_time', models.TimeField(default=datetime.time(12, 0))),
                ('current_count', models.PositiveSmallIntegerField(default=0)),
                ('total_count', models.PositiveSmallIntegerField(default=0)),
                ('poster', models.ImageField(null=True, storage=app.storage.OverwriteStorage(), upload_to=series.util.poster_path)),
                ('media_type_options', jsonfield.fields.JSONField(blank=True, help_text='A JSON object of options made available from the media type')),
                ('release_schedule', models.CharField(choices=[('N', 'None'), ('W', 'Weekly'), ('F', 'Fortnightly'), ('M', 'Monthly'), ('D', 'Discrete')], default='W', max_length=1)),
                ('release_schedule_options', jsonfield.fields.JSONField(blank=True, help_text='A JSON object of needed info for each type of release schedule')),
                ('media_type', models.ForeignKey(help_text="Series' media type", on_delete=django.db.models.deletion.CASCADE, to='series.MediaType')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Provider')),
            ],
        ),
    ]
