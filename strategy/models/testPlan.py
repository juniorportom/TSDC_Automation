from django.db import models
from datetime import datetime
from strategy.models.testStrategy import TestStrategy
from strategy.models.applicationScript import ApplicationScript
from strategy.models.browser import Browser
from strategy.models.mobileOS import MobileSO


class TestPlan(models.Model):
    STATUS_TYPES = (
        ('R', 'Registrado'),
        ('P', 'Programado'),
        ('E', 'Ejecutado')
    )
    description = models.CharField(max_length=250)
    browser = models.ManyToManyField(Browser, blank=True)
    mobile_so = models.ManyToManyField(MobileSO, blank=True)
    scripts = models.ManyToManyField(ApplicationScript, blank=True)
    execution_date = models.DateTimeField(default=datetime.now)
    create_at = models.DateTimeField(default=datetime.now)
    iterations = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default='P')
    test_strategy = models.ForeignKey(TestStrategy, on_delete=models.CASCADE)
    execute_immediately = models.BooleanField(default=True)

    def __str__(self):
        return self.description

    def browser_list(self):
        return self.browser.all()

    def mobile_list(self):
        return self.mobile_so.all()

    def script_list(self):
        return self.scripts.all()

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"
        ordering = ['-create_at']

