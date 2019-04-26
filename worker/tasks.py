from celery import Celery
import subprocess
import psycopg2
import pandas as pd
from boto3.s3.transfer import S3Transfer
import boto3
from datetime import datetime
import traceback

app = Celery('hello', broker='sqs://AKIAJ4VX226X4IHE5E7A:XUd1gR+JXsaPzTrF+czseE3fFaywyGhMJTZjZP7k@sqs.us-east-2.amazonaws.com/081242815322/celery')
app.conf.update(
            broker_transport_options = {'region': 'us-east-2'}
            )

@app.task
def add(x, y):
        return x + y

@app.task
def cypressHeadless(id):
        
        try:
            print('inicia con id='+str(id))

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, executed_date =%s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('E',now))

       
            subprocess.check_call('rm -fr cypress/integration/* && rm -rf mochawesome-report/ && rm -rf cypress/results_json/* && rm -rf cypress/results/*', shell=True)

            exceptionTest = connectSelect("SELECT * FROM strategy_testexecution WHERE id="+str(id))

            script_id = exceptionTest['script_id'][0]
            user = exceptionTest['user_id'][0]
            idScript = exceptionTest['id'][0]
           
            print('scrupy id ='+str(script_id))

            scriptTest = connectSelect("SELECT * FROM strategy_applicationscript WHERE id="+str(script_id))
            script_file = scriptTest['script_file'][0]

            print('Descargando script')

            #client = boto3.client('s3', aws_access_key_id='AKIAI4OSA7ESCGMIGGOQ', aws_secret_access_key='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')
            client = boto3.client('s3', aws_access_key_id='AKIAIU5JOSX7HQNXIFRA', aws_secret_access_key='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')
            client.download_file('tsdc-automation.media', script_file, 'cypress/integration/'+str(idScript)+'_spec.js')
            
            print('Ejecutando Script')
            subprocess.check_call('node_modules/.bin/cypress run', shell=True)
            subprocess.check_call('npx mochawesome-merge --reportDir cypress/results > cypress/results_json/mochawesome_report.json', shell=True)
            subprocess.check_call('npx mochawesome-report-generator --cdn=true --reportTitle=My_Custom_Title cypress/results_json/mochawesome_report.json', shell=True)


            nameReport = 'reports/'+str(user)+'/'+str(id)+'.html'
            #client = boto3.client('s3', aws_access_key_id='AKIAI4OSA7ESCGMIGGOQ', aws_secret_access_key='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')
            #client = boto3.client('s3', aws_access_key_id='AKIAIU5JOSX7HQNXIFRA', aws_secret_access_key='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')
            #transfer = S3Transfer(client)
            #transfer.upload_file('mochawesome-report/mochawesome_report.html', 'tsdc-automation.media', nameReport,ExtraArgs={'ACL':'public-read'})
            client.upload_file('/home/ubuntu/cypress/mochawesome-report/mochawesome_report.html', 'tsdc-automation.media', nameReport, ExtraArgs={'ACL':'public-read'})

            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, report_file = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('S',nameReport))
        
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('F'))
        
        return 4

@app.task
def monkeyHeadless(id):

        try:
            print('inicia con id='+str(id))

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, executed_date =%s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('E',now))


            exceptionTest = connectSelect("SELECT * FROM strategy_testexecution WHERE id="+str(id))

            script_id = exceptionTest['script_id'][0]
            user = exceptionTest['user_id'][0]
            idScript = exceptionTest['id'][0]

            print('scrupy id ='+str(script_id))

            scriptTest = connectSelect("SELECT * FROM strategy_applicationscript WHERE id="+str(script_id))
            script_file = scriptTest['script_file'][0]

            

            print('Ejecutando Script')
            subprocess.check_call('cd ~/gremlins-webdriver/ &&  npm test', shell=True)
            subprocess.check_call('cd ~/gremlins-webdriver/ &&  npx mochawesome-report-generator --cdn=true myfile.json', shell=True)



            nameReport = 'reports/'+str(user)+'/'+str(id)+'.html'
            #client = boto3.client('s3', aws_access_key_id='AKIAI4OSA7ESCGMIGGOQ', aws_secret_access_key='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')
            client = boto3.client('s3', aws_access_key_id='AKIAIU5JOSX7HQNXIFRA', aws_secret_access_key='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')
            #transfer = S3Transfer(client)
            #transfer.upload_file('mochawesome-report/mochawesome_report.html', 'tsdc-automation.media', nameReport,ExtraArgs={'ACL':'public-read'})
            client.upload_file('/home/ubuntu/gremlins-webdriver/mochawesome-report/myfile.html', 'tsdc-automation.media', nameReport, ExtraArgs={'ACL':'public-read'})

            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, report_file = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('S',nameReport))

        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('F'))

        return 4

@app.task
def monkeyCalabash(id):
    
    try:
        print('inicia con id='+str(id))

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, executed_date =%s  WHERE id = """+str(id)
        connectUpdate(sqlUpdate,('E',now))

        path = "~/Documentos/pruebas/proyecto/calabash"
        subprocess.call('cd '+path+' && rm  features/*.feature', shell=True)
        subprocess.call('cd '+path+' && rm *.png', shell=True)
        subprocess.call('cd '+path+' && rm reporte.html', shell=True)
        subprocess.call('cd '+path+' && rm test_servers/*.apk', shell=True)

        exceptionTest = connectSelect("SELECT * FROM strategy_testexecution WHERE id="+str(id))

        script_id = exceptionTest['script_id'][0]
        user = exceptionTest['user_id'][0]
        idScript = exceptionTest['id'][0]
        
        print('scrupy id ='+str(script_id))

        scriptTest = connectSelect("SELECT * FROM strategy_applicationscript WHERE id="+str(script_id))
        script_file = scriptTest['script_file'][0]

        print('Descargando script')

        client = boto3.client('s3', aws_access_key_id='AKIAIU5JOSX7HQNXIFRA', aws_secret_access_key='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')
        client.download_file('tsdc-automation.media', script_file, path+'/features/'+str(idScript)+'.fearure')
            
        print('Ejecutando Script')

        subprocess.check_call('cd '+path+' && calabash-android resign 5.5.1.apk', shell=True)
        subprocess.call('cd '+path+' && calabash-android run 5.5.1.apk --format html --out reporte.html', shell=True)
        
        nameReport = 'reports/'+str(user)+'/'+str(id)+'.html'
        
        client.upload_file(path+'/reporte.html', 'tsdc-automation.media', nameReport, ExtraArgs={'ACL':'public-read'})

        sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, report_file = %s  WHERE id = """+str(id)
        connectUpdate(sqlUpdate,('S',nameReport))
        
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        sqlUpdate = """ UPDATE strategy_testexecution SET status = %s  WHERE id = """+str(id)
        connectUpdate(sqlUpdate,('F'))


def connectSelect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    result = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="smarttoolsdb.cqbimrfyvxj0.us-east-2.rds.amazonaws.com",database="tsdc_automationdb", user="smartuser", password="CloudProyect1*")
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cols = list(map(lambda x: x[0], cur.description))
        result = pd.DataFrame(data, columns=cols)
        cur.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return result
            print('Database connection closed.')


def connectUpdate(query, param):
    """ update vendor name based on the vendor id """
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(host="smarttoolsdb.cqbimrfyvxj0.us-east-2.rds.amazonaws.com",database="tsdc_automationdb", user="smartuser", password="CloudProyect1*")
        cur = conn.cursor()
        cur.execute(query, param)
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return updated_rows


