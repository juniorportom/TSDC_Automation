from django.db import models


class ApplicationType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "type"
        verbose_name_plural = 'types'

