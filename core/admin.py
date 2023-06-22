from django.contrib import admin
from core import models


@admin.register(models.Doctor)
class Weather(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Appeal)
class Weather(admin.ModelAdmin):
    list_display = ('doctor', 'appeal_date', 'appeal_time', 'created_date')
