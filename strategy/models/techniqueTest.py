from django.db import models
from strategy.models.tool import Tool


class TechniqueTest(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Tool, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '/' + self.version

    class Meta:
        verbose_name_plural = 'mobiles_so'