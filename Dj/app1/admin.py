from django.contrib import admin
from .models import *

# Register your models here.


class NewmapInfo(admin.StackedInline): 
    model = imgout

@admin.register(newmap)
class AdminNewmap(admin.ModelAdmin):
    list_display = ["id", "imgdata", "timdata", "mapdata"]
    inlines = [NewmapInfo]

admin.site.register(userinfo)
admin.site.register(historyevent)