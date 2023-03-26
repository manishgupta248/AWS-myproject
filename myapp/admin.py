from import_export.admin import ImportExportModelAdmin  #keep it on Top
from django.contrib import admin
from .models import Notice

# Register your models here.

class NoticeAdmin(ImportExportModelAdmin):
    list_display = ['subject', 'notice_date', 'upload_on', 'notice_copy', 'upload_by',]

admin.site.register(Notice, NoticeAdmin)