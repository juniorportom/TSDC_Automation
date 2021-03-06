from django.contrib import admin
from strategy.models.applicationType import ApplicationType
from strategy.models.application import Application
from strategy.models.tool import Tool
from strategy.models.browser import Browser
from strategy.models.mobileOS import MobileSO
from strategy.models.techniqueTest import TechniqueTest
from strategy.models.applicationVersion import ApplicationVersion
from strategy.models.testStrategy import TestStrategy
from strategy.models.testPlan import TestPlan
from strategy.models.testExecution import TestExecution

# Register your models here.
admin.site.register(ApplicationType)
admin.site.register(Application)
admin.site.register(Tool)
admin.site.register(Browser)
admin.site.register(MobileSO)
admin.site.register(TechniqueTest)
admin.site.register(ApplicationVersion)
admin.site.register(TestStrategy)
admin.site.register(TestPlan)
admin.site.register(TestExecution)
