from celery import Celery
import subprocess
import psycopg2
import pandas as pd
from boto3.s3.transfer import S3Transfer
import boto3
from datetime import datetime

app = Celery('hello', broker='sqs://@sqs.us-east-2.amazonaws.com//celery')
app.conf.update(
            broker_transport_options = {'region': 'us-east-2'}
            )

@app.task
def add(x, y):
        return x + y

@app.task
def cypressHeadless(id):
        try:
        
            subprocess.check_call('rm -fr cypress/integration/* && rm -rf mochawesome-report/ && rm -rf cypress/results_json/* && rm -rf cypress/results/*', shell=True)

            exceptionTest = connectSelect("SELECT * FROM strategy_testexecution WHERE id="+str(id))

            script_id = exceptionTest['script_id'][0]
            user = exceptionTest['user_id'][0]
            idScript = exceptionTest['id'][0]

            scriptTest = connectSelect("SELECT * FROM strategy_applicationscript WHERE id="+str(idScript))
            script_file = scriptTest['script_file'][0]
            now = datetime.now()

            timestamp = datetime.timestamp(now)
            print(timestamp)
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, executed_date =%s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('E',now))

            
            client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
            client.download_file('tsdc-automation.media', script_file, 'cypress/integration/'+str(idScript)+'_spec.js')
 
            subprocess.check_call('node_modules/.bin/cypress run', shell=True)
            subprocess.check_call('npx mochawesome-merge --reportDir cypress/results > cypress/results_json/mochawesome_report.json', shell=True)
            subprocess.check_call('npx mochawesome-report-generator --cdn=true --reportTitle=My_Custom_Title cypress/results_json/mochawesome_report.json', shell=True)


            nameReport = 'reports/'+str(user)+'/'+str(id)+'.html'

            client.upload_file('/home/ubuntu/cypress/mochawesome-report/mochawesome_report.html', 'tsdc-automation.media', nameReport, ExtraArgs={'ACL':'public-read'})

            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s, report_file = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('S',nameReport))
        
        except:
            sqlUpdate = """ UPDATE strategy_testexecution SET status = %s  WHERE id = """+str(id)
            connectUpdate(sqlUpdate,('F'))
        
        return 4


def connectSelect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    result = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="",database="", user="", password="")
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
        conn = psycopg2.connect(host="",database="", user="", password="")
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
