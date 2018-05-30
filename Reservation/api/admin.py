from django.contrib import admin
from .models import Date, Room, Time
# Register your models here.

class RoomInLine(admin.StackedInline):
    model = Room
    extra = 0

class TimeInLine(admin.StackedInline):
    model = Time
    extra = 0

class DateAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields':['study_date']}),
            ('Date Information', {'fields' : ['room_size']}),
        ]
    inlines = [RoomInLine]


admin.site.register(Date, DateAdmin)
admin.site.register(Time)
