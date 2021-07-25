from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from testapp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']
admin.site.register(Movie,ModelAdmin)