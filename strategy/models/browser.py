from django.db import models


class Browser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "browser"
        verbose_name_plural = 'browsers'
