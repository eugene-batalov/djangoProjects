#!/usr/bin/env python3
from django.contrib import admin
from .models import *


class AccAdmin(admin.ModelAdmin):
    list_display = ('userid','puzzle', 'downloaddt', 'answerdt', 'ipaddress', 'useragent', 'nicetries')
    list_filter = ('puzzle','userid')

class UserChoiceInline(admin.StackedInline):
    model = Payments
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'nickname', 'name', 'lastname', 'country', 'language', 'gender', 'birthdate', 'email', 'phone', 'billinginfo', 'zone2rating', 'zone3rating', 'sendnews', 'emailconfirmed')
    inlines = [UserChoiceInline]    
    
admin.site.register(Users)
#admin.site.register(Users, UserAdmin)
admin.site.register(Tournaments)
admin.site.register(Puzzles)
admin.site.register(Pictures)
admin.site.register(Payments)
admin.site.register(News)
admin.site.register(Localization)
admin.site.register(Levelpoints)
admin.site.register(Languages)
admin.site.register(Groups)
admin.site.register(Countries)
admin.site.register(Complexity)
admin.site.register(Access, AccAdmin)
