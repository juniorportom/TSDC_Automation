from celery import Celery
from django.conf import settings
import os


def send_message(function_name, id_exec):
    str_conn = 'sqs://' + settings.AWS_ACCESS_KEY_ID_SQS + ':' + settings.AWS_SECRET_ACCESS_KEY_SQS + '@' + \
               os.environ["URL_NAME_SQS"]
    app = Celery('hello', broker=str_conn)

    app.conf.update(
        broker_transport_options={'region': 'us-east-2'}
    )
    app.send_task('tasks.' + function_name, kwargs={'id': id_exec})

