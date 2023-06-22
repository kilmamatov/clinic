from django.contrib import admin
from core import models


@admin.register(models.Doctor)
class Weather(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Appointment)
class Weather(admin.ModelAdmin):
    list_display = ('doctor', 'created_date')
