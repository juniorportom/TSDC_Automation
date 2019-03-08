from django.db import models
from datetime import datetime
from strategy.models.testPlan import TestPlan


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

    def __str__(self):
        return self.iteration

    class Meta:
        verbose_name = "execution"
        verbose_name_plural = "executions"
        ordering = ['-execution_date']

    def report_name(self):
        return self.report_file.name.replace('reports/', '')

    def get_absolute_report_url(self):
        # return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/'+str(self.script_file.name)
        return self.report_file.url
