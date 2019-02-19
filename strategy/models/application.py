from django.db import models
from datetime import datetime
from .applicationType import ApplicationType


class Application(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(ApplicationType, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    architecture = models.CharField(max_length=300)
    developer_stack = models.CharField(max_length=300)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "application"
        verbose_name_plural = "applications"
        ordering = ['-create_at']
