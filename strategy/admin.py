from django.contrib import admin
from strategy.models.applicationType import ApplicationType
from strategy.models.application import Application

# Register your models here.
admin.site.register(ApplicationType)
admin.site.register(Application)
