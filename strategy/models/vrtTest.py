from django.db import models
from datetime import datetime
from strategy.models.stepImage import StepImage


class VrtTest(models.Model):
    step_image_a = models.ForeignKey(StepImage, on_delete=models.CASCADE, related_name='image1')
    step_image_b = models.ForeignKey(StepImage, on_delete=models.CASCADE, related_name='image2')
    image_diff = models.CharField(max_length=500)
    data = models.CharField(max_length=500)
    create_at = models.DateTimeField(default=datetime.now)

    def get_absolute_img_diff_url(self):
        return self.image_diff

    class Meta:
        verbose_name = "regression"
        verbose_name_plural = "regressions"
        ordering = ['-create_at']
