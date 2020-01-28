from django.contrib import admin

from app_one.models import Topic, Webpage, AccessRecord, UserInfo

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserInfo)
