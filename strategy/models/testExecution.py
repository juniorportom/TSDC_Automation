from django.db import models
from datetime import datetime
from strategy.models.testPlan import TestPlan
from strategy.models.applicationScript import ApplicationScript
from strategy.models.browser import Browser
from strategy.models.mobileOS import MobileSO
from django.contrib.auth.models import User


class TestExecution(models.Model):
    STATUS_TYPES = (
        ('P', 'Programado'),
        ('E', 'En ejecución'),
        ('S', 'Exitoso'),
        ('F', 'Fallido')
    )
    test_plan = models.ForeignKey(TestPlan, on_delete=models.CASCADE)
    iteration = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default='P')
    report_file = models.FileField(upload_to='reports/', null=True, blank=True)
    execution_date = models.DateTimeField(default=datetime.now)
    executed_date = models.DateTimeField(blank=True, null=True)
    browser = models.ForeignKey(Browser, on_delete=models.CASCADE, blank=True, null=True)
    mobile_so = models.ForeignKey(MobileSO, on_delete=models.CASCADE, blank=True, null=True)
    script = models.ForeignKey(ApplicationScript, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.iteration

    class Meta:
        verbose_name = "execution"
        verbose_name_plural = "executions"
        ordering = ['-execution_date']

    def report_name(self):
        return self.report_file.name.replace('reports/', '')

    def get_absolute_report_url(self):
        return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/'+str(self.report_file.name)
        # return self.report_file.url
