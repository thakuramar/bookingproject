from django.contrib import admin
from .import models
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]


admin.site.register(models.Notice, NoticeAdmin)
