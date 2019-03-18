from django.db import models
from datetime import datetime
from .application import Application
from strategy.models.techniqueTest import TechniqueTest
from django.contrib.auth.models import User


def custom_upload_to(instance, filename):
    print(filename)
    if instance.pk:
        old_instance = ApplicationScript.objects.get(pk=instance.pk)
        if old_instance:
            old_instance.script_file.delete()
    app = Application.objects.get(pk=instance.application.id)
    user = User.objects.get(pk=app.user.id)
    return 'scripts/' + user.username + '/' + app.name.strip().replace(' ', '_') + '/' + filename


class ApplicationScript(models.Model):
    name = models.CharField(max_length=100)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    script_file = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    technique_test = models.ForeignKey(TechniqueTest, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + ' - ' + self.technique_test.__str__()

    def script_name(self):
        name = self.script_file.name.split('/')
        return name.pop()

    def get_absolute_script_url(self):
        return 'https://s3.us-east-2.amazonaws.com/tsdc-automation.media/'+str(self.script_file.name)
        # return self.script_file.url

    class Meta:
        verbose_name = "script"
        verbose_name_plural = "scripts"
        ordering = ['-create_at']
