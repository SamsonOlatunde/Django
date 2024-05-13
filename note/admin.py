from django.contrib import admin
from . import models

class ModelAdmin(admin.ModelAdmin):
    list_display = ('title',)



admin.site.register(models.Note, ModelAdmin)
