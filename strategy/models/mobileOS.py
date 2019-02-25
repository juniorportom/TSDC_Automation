from django.db import models


class MobileSO(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)

    def __str__(self):
        return self.name + '/' + self.version

    class Meta:
        verbose_name_plural = 'mobiles'