from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tool"
        verbose_name_plural = 'tools'
