from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from .applicationType import ApplicationType


class Application(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(ApplicationType, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    architecture = models.CharField(max_length=300)
    developer_stack = models.CharField(max_length=300)
    create_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "application"
        verbose_name_plural = "applications"
        ordering = ['-create_at']

    def is_mobile(self):
        if self.type.name == 'Mobile':
            return True
        return False




