from django.db import models
from strategy.models.testExecution import TestExecution


def custom_upload_to(instance, filename):
    print(filename)
    if instance.pk:
        old_instance = StepImage.objects.get(pk=instance.pk)
        if old_instance:
            old_instance.image.delete()
    exec_test = TestExecution.objects.get(pk=instance.test_execution.id)
    return 'steps/' + str(exec_test.id) + '/' + filename


class StepImage(models.Model):
    image = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    test_execution = models.ForeignKey(TestExecution, on_delete=models.CASCADE)

    def image_name(self):
        name = self.image.name.split('/')
        return name.pop()

    def get_absolute_img_url(self):
        # return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/' + str(self.image.name)
        return 'https://d375j7oj9wi0ea.cloudfront.net/' + str(self.image.name)
        # return self.image.url

    def get_absolute_s3_img_url(self):
        return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/' + str(self.image.name)

    class Meta:
        verbose_name = "image_step"
        verbose_name_plural = "image_steps"
