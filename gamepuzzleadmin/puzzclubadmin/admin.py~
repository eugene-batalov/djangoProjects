from django.contrib import admin
from .models import *


class AccessAdmin(admin.ModelAdmin):
    list_display = ('userid', 'puzzle', 'downloaddt', 'answerdt', 'ipaddress', 'useragent', 'nicetries')
    list_filter = ('puzzle','userid')
    
admin.site.register(Users)
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
admin.site.register(Access, AccessAdmin)
