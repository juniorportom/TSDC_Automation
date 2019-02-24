from django.db import models
from datetime import datetime
from .application import Application


class ApplicationVersion(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    version = models.CharField(max_length=200)
    url_repository = models.CharField(max_length=250, null=True)
    create_at = models.DateTimeField(default=datetime.now)
    # build_package = models.CharField(max_length=250)

    def __str__(self):
        return self.application.name + '/' + self.version

    class Meta:
        verbose_name = "version"
        verbose_name_plural = "versions"
        ordering = ['-create_at']