# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_text


class Acces(models.Model):
    accessid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    puzzle = models.ForeignKey('Puzzle', models.DO_NOTHING, db_column='puzzle')
    downloaddt = models.DateTimeField(blank=True, null=True)
    answerdt = models.DateTimeField(blank=True, null=True)
    ipaddress = models.CharField(max_length=40)
    useragent = models.CharField(max_length=200)
    nicetries = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Access'


class Complexity(models.Model):
    complexityid = models.AutoField(primary_key=True)
    horizontalelements = models.IntegerField()
    level = models.IntegerField()
    verticalelements = models.IntegerField()
    zone2points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Complexity'


class Countrie(models.Model):
    countryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Countries'


class Group(models.Model):
    groupid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Groups'


class Language(models.Model):
    languageid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Languages'


class Levelpoint(models.Model):
    levelpointsid = models.AutoField(primary_key=True)
    place1points = models.IntegerField(blank=True, null=True)
    place2points = models.IntegerField(blank=True, null=True)
    place3points = models.IntegerField(blank=True, null=True)
    place4points = models.IntegerField(blank=True, null=True)
    place5points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Levelpoints'


class Localization(models.Model):
    keyword = models.CharField(db_column='Keyword', primary_key=True, max_length=50)  # Field name made lowercase.
    russian = models.CharField(db_column='Russian', max_length=1000)  # Field name made lowercase.
    english = models.CharField(db_column='English', max_length=1000)  # Field name made lowercase.
    german = models.CharField(db_column='German', max_length=1000)  # Field name made lowercase.
    french = models.CharField(db_column='French', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Localization'


class New(models.Model):
    newsid = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    header = models.CharField(max_length=100)
    img = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'News'


class Payment(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    zone = models.IntegerField()
    docnum = models.CharField(max_length=100, blank=True, null=True)
    paydate = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    zone2periodstart = models.DateField(blank=True, null=True)
    zone2periodend = models.DateField(blank=True, null=True)
    zone3tournament = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='zone3tournament', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Payments'


class Picture(models.Model):
    pictureid = models.AutoField(primary_key=True)
    width = models.IntegerField()
    height = models.IntegerField()
    picturedata = models.TextField()

    class Meta:
        managed = False
        db_table = 'Pictures'


class Puzzle(models.Model):
    puzzleid = models.AutoField(primary_key=True)
    puzzledata = models.TextField()
    picture = models.ForeignKey(Picture, models.DO_NOTHING, db_column='picture')
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid')
    zone = models.IntegerField()
    complexity = models.ForeignKey(Complexity, models.DO_NOTHING, db_column='complexity')
    task = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    icon = models.TextField()

    class Meta:
        managed = False
        db_table = 'Puzzles'


class Tournament(models.Model):
    tournamentid = models.AutoField(primary_key=True)
    startdatetime = models.DateTimeField()
    level = models.ForeignKey(Levelpoint, models.DO_NOTHING, db_column='level')
    puzzle = models.ForeignKey(Puzzle, models.DO_NOTHING, db_column='puzzle')
    tourpass = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prizepercent = models.DecimalField(max_digits=5, decimal_places=2)
    place1user = models.ForeignKey('User', models.DO_NOTHING, db_column='place1user', blank=True, null=True, related_name='place1user')
    place2user = models.ForeignKey('User', models.DO_NOTHING, db_column='place2user', blank=True, null=True, related_name='place2user')
    place3user = models.ForeignKey('User', models.DO_NOTHING, db_column='place3user', blank=True, null=True, related_name='place3user')
    place4user = models.ForeignKey('User', models.DO_NOTHING, db_column='place4user', blank=True, null=True, related_name='place4user')
    place5user = models.ForeignKey('User', models.DO_NOTHING, db_column='place5user', blank=True, null=True, related_name='place5user')
    notificationsent = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tournaments'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    nickname = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    userpass = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Countrie, models.DO_NOTHING, db_column='country')
    language = models.ForeignKey(Language, models.DO_NOTHING, db_column='language')
    gender = models.CharField(max_length=1, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45, blank=True, null=True)
    billinginfo = models.TextField(blank=True, null=True)
    zone2rating = models.IntegerField(blank=True, null=True)
    zone3rating = models.IntegerField(blank=True, null=True)
    sendnews = models.CharField(max_length=1, blank=True, null=True)
    emailconfirmed = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Users'
