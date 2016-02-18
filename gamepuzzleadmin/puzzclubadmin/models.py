#!/usr/bin/env python3
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Access(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    puzzle = models.IntegerField()
    downloaddt = models.DateTimeField(blank=True, null=True)
    answerdt = models.DateTimeField(blank=True, null=True)
    ipaddress = models.TextField(blank=True, null=True)
    useragent = models.TextField(blank=True, null=True)
    nicetries = models.IntegerField()
    accessid = models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.accessid)    
    
    class Meta:
        managed = False
        db_table = 'Access'


class Complexity(models.Model):
    complexityid = models.AutoField(primary_key=True)
    horizontalelements = models.IntegerField()
    level = models.IntegerField()
    verticalelements = models.IntegerField()
    zone2points = models.IntegerField()
    def __str__(self):
        return str(self.complexityid)
        
    class Meta:
        managed = False
        db_table = 'Complexity'


class Countries(models.Model):
    countryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=45)
    def __str__(self):
        return str(self.name)

    class Meta:
        managed = False
        db_table = 'Countries'


class Groups(models.Model):
    groupid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

    class Meta:
        managed = False
        db_table = 'Groups'


class Languages(models.Model):
    languageid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=45)
    def __str__(self):
        return str(self.name)
        
    class Meta:
        managed = False
        db_table = 'Languages'


class Levelpoints(models.Model):
    levelpointsid = models.AutoField(primary_key=True)
    place1points = models.IntegerField(blank=True, null=True)
    place2points = models.IntegerField(blank=True, null=True)
    place3points = models.IntegerField(blank=True, null=True)
    place4points = models.IntegerField(blank=True, null=True)
    place5points = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.levelpointsid)
        
    class Meta:
        managed = False
        db_table = 'Levelpoints'


class Localization(models.Model):
    keyword = models.CharField(db_column='Keyword', primary_key=True, max_length=50)  # Field name made lowercase.
    russian = models.CharField(db_column='Russian', max_length=1000)  # Field name made lowercase.
    english = models.CharField(db_column='English', max_length=1000)  # Field name made lowercase.
    german = models.CharField(db_column='German', max_length=1000)  # Field name made lowercase.
    french = models.CharField(db_column='French', max_length=1000)  # Field name made lowercase.
    def __str__(self):
        return str(self.keyword)
        
    class Meta:
        managed = False
        db_table = 'Localization'


class News(models.Model):
    newsid = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    header = models.CharField(max_length=100)
    img = models.ImageField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    def __str__(self):
        return str(self.content)
        
    class Meta:
        managed = False
        db_table = 'News'


class Payments(models.Model):
    paymentid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    zone = models.IntegerField()
    docnum = models.CharField(max_length=100, blank=True, null=True)
    paydate = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    zone2periodstart = models.DateField(blank=True, null=True)
    zone2periodend = models.DateField(blank=True, null=True)
    zone3tournament = models.ForeignKey('Tournaments', models.DO_NOTHING, db_column='zone3tournament', blank=True, null=True)
    def __str__(self):
        return str(self.paymentid)
        
    class Meta:
        managed = False
        db_table = 'Payments'


class Pictures(models.Model):
    pictureid = models.AutoField(primary_key=True)
    width = models.IntegerField()
    height = models.IntegerField()
    picturedata = models.ImageField()
    def __str__(self):
        return str(self.pictureid)
        
    class Meta:
        managed = False
        db_table = 'Pictures'


class Puzzles(models.Model):
    puzzleid = models.AutoField(primary_key=True)
    puzzledata = models.ImageField()
    picture = models.ForeignKey(Pictures, models.DO_NOTHING, db_column='picture')
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid')
    zone = models.IntegerField()
    complexity = models.ForeignKey(Complexity, models.DO_NOTHING, db_column='complexity')
    task = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    icon = models.ImageField()
    def __str__(self):
        return str(self.puzzleid)
        
    class Meta:
        managed = False
        db_table = 'Puzzles'


class Tournaments(models.Model):
    tournamentid = models.AutoField(primary_key=True)
    startdatetime = models.DateTimeField()
    level = models.ForeignKey(Levelpoints, models.DO_NOTHING, db_column='level')
    puzzle = models.ForeignKey(Puzzles, models.DO_NOTHING, db_column='puzzle')
    tourpass = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prizepercent = models.DecimalField(max_digits=5, decimal_places=2)
    place1user = models.ForeignKey('Users', models.DO_NOTHING, db_column='place1user', blank=True, null=True, related_name='place1user')
    place2user = models.ForeignKey('Users', models.DO_NOTHING, db_column='place2user', blank=True, null=True, related_name='place2user')
    place3user = models.ForeignKey('Users', models.DO_NOTHING, db_column='place3user', blank=True, null=True, related_name='place3user')
    place4user = models.ForeignKey('Users', models.DO_NOTHING, db_column='place4user', blank=True, null=True, related_name='place4user')
    place5user = models.ForeignKey('Users', models.DO_NOTHING, db_column='place5user', blank=True, null=True, related_name='place5user')
    notificationsent = models.CharField(max_length=1, blank=True, null=True)
    def __str__(self):
        return str(self.tournamentid)
        
    class Meta:
        managed = False
        db_table = 'Tournaments'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    nickname = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    userpass = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='country')
    language = models.ForeignKey(Languages, models.DO_NOTHING, db_column='language')
    gender = models.CharField(max_length=1, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45, blank=True, null=True)
    billinginfo = models.TextField(blank=True, null=True)
    zone2rating = models.IntegerField(blank=True, null=True)
    zone3rating = models.IntegerField(blank=True, null=True)
    sendnews = models.CharField(max_length=1, blank=True, null=True)
    emailconfirmed = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)
        
    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
