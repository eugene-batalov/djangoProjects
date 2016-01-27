# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzclubadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acces',
            fields=[
                ('accessid', models.AutoField(primary_key=True, serialize=False)),
                ('downloaddt', models.DateTimeField(blank=True, null=True)),
                ('answerdt', models.DateTimeField(blank=True, null=True)),
                ('ipaddress', models.CharField(max_length=40)),
                ('useragent', models.TextField(blank=True, null=True)),
                ('nicetries', models.IntegerField()),
            ],
            options={
                'db_table': 'Access',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countrie',
            fields=[
                ('countryid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('languageid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Levelpoint',
            fields=[
                ('levelpointsid', models.AutoField(primary_key=True, serialize=False)),
                ('place1points', models.IntegerField(blank=True, null=True)),
                ('place2points', models.IntegerField(blank=True, null=True)),
                ('place3points', models.IntegerField(blank=True, null=True)),
                ('place4points', models.IntegerField(blank=True, null=True)),
                ('place5points', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Levelpoints',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('newsid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('header', models.CharField(max_length=100)),
                ('img', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'News',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.IntegerField()),
                ('docnum', models.CharField(blank=True, max_length=100, null=True)),
                ('paydate', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('zone2periodstart', models.DateField(blank=True, null=True)),
                ('zone2periodend', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Payments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('pictureid', models.AutoField(primary_key=True, serialize=False)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('picturedata', models.TextField()),
            ],
            options={
                'db_table': 'Pictures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('puzzleid', models.AutoField(primary_key=True, serialize=False)),
                ('puzzledata', models.TextField()),
                ('zone', models.IntegerField()),
                ('task', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('icon', models.TextField()),
            ],
            options={
                'db_table': 'Puzzles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tournamentid', models.AutoField(primary_key=True, serialize=False)),
                ('startdatetime', models.DateTimeField()),
                ('tourpass', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('prizepercent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notificationsent', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'Tournaments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('userpass', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('email', models.CharField(max_length=45)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('billinginfo', models.TextField(blank=True, null=True)),
                ('zone2rating', models.IntegerField(blank=True, null=True)),
                ('zone3rating', models.IntegerField(blank=True, null=True)),
                ('sendnews', models.CharField(blank=True, max_length=1, null=True)),
                ('emailconfirmed', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
    ]