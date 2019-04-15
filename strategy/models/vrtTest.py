from django.db import models
from strategy.models.stepImage import StepImage


def custom_upload_to(instance, filename):
    print(filename)
    if instance.pk:
        old_instance = VrtTest.objects.get(pk=instance.pk)
        if old_instance:
            old_instance.image.delete()
    img_a = StepImage.objects.get(pk=instance.step_image_a.id)
    img_b = StepImage.objects.get(pk=instance.step_image_b.id)
    return 'regressions/' + str(img_a.id) + '_' + str(img_b.id) + '/' + filename


class VrtTest(models.Model):
    step_image_a = models.ForeignKey(StepImage, on_delete=models.CASCADE)
    step_image_b = models.ForeignKey(StepImage, on_delete=models.CASCADE)
    image_diff = models.FileField(upload_to=custom_upload_to, null=True, blank=True)

    def image_name(self):
        name = self.image_diff.name.split('/')
        return name.pop()

    def get_absolute_script_url(self):
        # return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/' + str(self.image_diff.name)
        return 'https://d375j7oj9wi0ea.cloudfront.net/' + str(self.image_diff.name)
        # return self.image_diff.url

    class Meta:
        verbose_name = "regression"
        verbose_name_plural = "regressions"
