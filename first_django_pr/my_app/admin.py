from django.contrib import admin
from .models import WeekDay
# Register your models here.
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'note')

admin.site.register(WeekDay, WeekDayAdmin)