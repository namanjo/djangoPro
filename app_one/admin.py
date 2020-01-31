from django.contrib import admin

from app_one.models import Topic, Webpage, AccessRecord, UserInfo, UserProfileRegister

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserInfo)
admin.site.register(UserProfileRegister)
