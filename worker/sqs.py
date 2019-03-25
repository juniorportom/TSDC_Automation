from celery import Celery

app = Celery('hello', broker='sqs://code:key@sqs.us-east-2.amazonaws.com')

app.conf.update(
                    broker_transport_options = {'region': 'us-east-2'}
                    )
app.send_task('tasks.cypressHeadless', kwargs={ 'id': 1})


#import boto3
#import json
#import base64

#message = {"headers":{"task":"cypressHeadless","args":['1'], "id":'1254785'}}

#message_string = json.dumps(message)
#byte_message = base64.b64encode(message_string.encode('utf-8'))
#base64_json_string = byte_message.decode()

#sqs = boto3.client('sqs',aws_access_key_id='',aws_secret_access_key='',region_name='us-east-2')
#queue_url = 'https://sqs.us-east-2.amazonaws.com'
#response = sqs.send_message(QueueUrl=queue_url,MessageAttributes={},MessageBody=(base64_json_string) )

