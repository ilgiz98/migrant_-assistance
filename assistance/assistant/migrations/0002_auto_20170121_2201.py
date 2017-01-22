# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 16:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assistant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
        migrations.AddField(
            model_name='document',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_region', to='assistant.Region', verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='document',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_post', to='assistant.Post', verbose_name='\u0417\u0430\u043f\u0438\u0441\u044c'),
        ),
    ]
