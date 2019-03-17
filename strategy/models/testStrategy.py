from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from strategy.models.applicationVersion import ApplicationVersion


class TestStrategy(models.Model):
    TEST_LEVEL_TYPES = (
        ('U', 'Unidad'),
        ('I', 'Integración'),
        ('S', 'Sistema'),
        ('A', 'Aceptación')
    )
    name = models.CharField(max_length=200)
    test_level = models.CharField(max_length=1, choices=TEST_LEVEL_TYPES)
    objective = models.CharField(max_length=500)
    application_version = models.ForeignKey(ApplicationVersion, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_application_type(self):
        print('En el modelo: ' + self.application_version.application.type)
        return self.application_version.application.type

    class Meta:
        verbose_name = "strategy"
        verbose_name_plural = "strategies"
        ordering = ['-create_at']
