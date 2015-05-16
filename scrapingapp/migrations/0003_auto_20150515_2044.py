# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapingapp', '0002_remove_outlet_wtf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publication_date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(to='scrapingapp.Writer'),
        ),
        migrations.AddField(
            model_name='article',
            name='outlet',
            field=models.ForeignKey(to='scrapingapp.Outlet'),
        ),
    ]
