from django.db import models
from datetime import datetime
from strategy.models.testStrategy import TestStrategy
from strategy.models.techniqueTest import TechniqueTest
from strategy.models.browser import Browser
from strategy.models.mobileOS import MobileSO


class TestPlan(models.Model):
    STATUS_TYPES = (
        ('R', 'Registrado'),
        ('P', 'Programado'),
        ('E', 'Ejecutado')
    )
    description = models.CharField(max_length=250)
    technique_test = models.ForeignKey(TechniqueTest, on_delete=models.CASCADE)
    browser = models.ForeignKey(Browser, on_delete=models.CASCADE, null=True, blank=True)
    mobile_so = models.ForeignKey(MobileSO, on_delete=models.CASCADE, null=True, blank=True)
    script_file = models.FileField(upload_to='scripts/', null=True, blank=True)
    execution_date = models.DateTimeField(default=datetime.now)
    create_at = models.DateTimeField(default=datetime.now)
    iterations = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_TYPES, default='R')
    test_strategy = models.ForeignKey(TestStrategy, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"
        ordering = ['-create_at']

    def script_name(self):
        return self.script_file.name.replace('scripts/', '')

    def get_absolute_script_url(self):
        # return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/'+str(self.script_file.name)
        return self.script_file.url
