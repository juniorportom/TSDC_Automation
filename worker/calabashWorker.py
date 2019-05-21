from celery import Celery
import subprocess
import os
from boto3.s3.transfer import S3Transfer
import boto3
from datetime import datetime
import traceback

from sqltt import *
from saveImages import *

#./emulator -avd Nexus_5X_API_26 -no-audio -no-window
#cd ~/Android/Sdk/emulator/
#java -jar target/MDroidPlus-1.0.0.jar libs4ast/ ~/Documentos/pruebas/taller8/gnucash-android/ org.gnucash.android tmp/mutants/ tmp/../ true
app = Celery('hello', broker='sqs://'+os.environ["AWS_ACCESS_KEY_ID_SQS"]+':'+os.environ["AWS_SECRET_ACCESS_KEY_SQS"]+'@sqs.us-east-2.amazonaws.com/081242815322/celery')
app.conf.update(
            broker_transport_options = {'region': 'us-east-2'}
            )


@app.task
def calabashHeadless(id):

        path = "~/Documentos/pruebas/proyecto/calabash"
        try:
            print('inicia con id='+str(id))

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, executed_date =%s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('E',now))

            
            subprocess.call('cd '+path+' && rm  features/*.feature', shell=True)
            subprocess.call('cd '+path+' && rm screenshot/*.png', shell=True)
            subprocess.call('cd '+path+' && rm reporte.html', shell=True)
            subprocess.call('cd '+path+' && rm test_servers/*.apk', shell=True)

            exceptionTest = connectSelect("SELECT * FROM strategy_testexecution WHERE id="+str(id))

            script_id = exceptionTest['script_id'][0]
            user = exceptionTest['user_id'][0]
            idScript = exceptionTest['id'][0]
            
            print('scrupy id ='+str(script_id))

            scriptTest = connectSelect("SELECT * FROM strategy_applicationscript WHERE id="+str(script_id))
            script_file = scriptTest['script_file'][0]

            print('Descargando scripttttt--->'+script_file)

            client = boto3.client('s3', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"], aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
            client.download_file('tsdc-automation.media', script_file, 'calabash/features/'+str(idScript)+'.feature')

                
            print('Ejecutando Script')

            subprocess.check_call('cd '+path+' && calabash-android resign 5.5.1.apk', shell=True)
            subprocess.call('cd '+path+' && SCREENSHOT_PATH=./screenshot/ calabash-android run 5.5.1.apk --format html --out reporte.html', shell=True)
            
            nameReport = 'reports/'+str(user)+'/'+str(id)+'.html'
            
            client.upload_file('calabash/reporte.html', 'tsdc-automation.media', nameReport, ExtraArgs={'ACL':'public-read'})

            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, report_file = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('S',nameReport))
            
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('F'))

        save_images(id,'/home/intraway/Documentos/pruebas/proyecto/calabash/screenshot/')
        return 4



@app.task
def mutationWorker(id):

        pathMut = "~/Documentos/pruebas/MutAPK"
        subprocess.call('cd '+pathMut+' && rm -rf mutants/*', shell=True)
        subprocess.check_call('cd '+pathMut+' && java -jar target/MutAPK-0.0.1.jar ../MutAPK/5.5.1.apk it.feio.android.omninote mutants/ extra/ . false', shell=True)

        path = "~/Documentos/pruebas/proyecto/calabash"
        try:
            print('inicia con id='+str(id))

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, executed_date =%s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('E',now))

            
            subprocess.call('cd '+path+' && rm  features/*.feature', shell=True)
            subprocess.call('cd '+path+' && rm screenshot/*.png', shell=True)
            subprocess.call('cd '+path+' && rm reporte.html', shell=True)
            subprocess.call('cd '+path+' && rm test_servers/*.apk', shell=True)

            exceptionTest = connectSelect("SELECT * FROM strategy_testexecution WHERE id="+str(id))

            script_id = exceptionTest['script_id'][0]
            user = exceptionTest['user_id'][0]
            idScript = exceptionTest['id'][0]
            
            print('scrupy id ='+str(script_id))

            scriptTest = connectSelect("SELECT * FROM strategy_applicationscript WHERE id="+str(script_id))
            script_file = scriptTest['script_file'][0]

            print('Descargando scripttttt--->'+script_file)

            client = boto3.client('s3', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"], aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
            client.download_file('tsdc-automation.media', script_file, 'calabash/features/'+str(idScript)+'.feature')

            print('Ejecutando Script')

            subprocess.check_call('cd '+path+' && calabash-android resign ../../MutAPK/mutants/it.feio.android.omninote-mutant1/5.5.1.apk', shell=True)
            subprocess.call('cd '+path+' && SCREENSHOT_PATH=./screenshot/ calabash-android run ../../MutAPK/mutants/it.feio.android.omninote-mutant1/5.5.1.apk --format html --out reporte.html', shell=True)
            
            nameReport = 'reports/'+str(user)+'/'+str(id)+'.html'
            
            client.upload_file('calabash/reporte.html', 'tsdc-automation.media', nameReport, ExtraArgs={'ACL':'public-read'})

            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, report_file = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('S',nameReport))
            
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('F'))

        save_images(id,'/home/intraway/Documentos/pruebas/proyecto/calabash/screenshot/')
        return 4
        