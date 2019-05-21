import boto3
import psycopg2
import os
from pathlib import Path


def save_images(exc_id, path_images=Path.cwd()):
    for img in Path(path_images).iterdir():
        if img.is_file():
            save_s3_img(exc_id, img.name, path_images)
            save_step(exc_id, img.name)
    print("Se completan inserciones")


def save_step(exc_id, img):
    conn = psycopg2.connect(host=os.environ["DB_HOSTNAME"], database=os.environ["DB_NAME"], user=os.environ["DB_USER"],
                            password=os.environ["DB_PASSWORD"], port=os.environ["DB_PORT"])
    cur = conn.cursor()
    img_name = 'steps/'+str(exc_id)+'/'+str(img)
    cur.execute('insert into strategy_stepimage (image, test_execution_id)  values ('+ '\'' + str(img_name) + '\'' + ', '+str(exc_id) +');')
    print("Se inserta imagen: " + str(img))
    conn.commit()
    cur.close()
    conn.close()


def save_s3_img(exc_id, img, path):
    client = boto3.client('s3', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"], aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
    img_name_s3 = 'steps/'+str(exc_id)+'/'+str(img)
    client.upload_file(str(path)+str(img), 'tsdc-automation.media', img_name_s3, ExtraArgs={'ACL': 'public-read'})
    print("Se alamcena en s3 imagen: " + str(img))


#save_images(26, '/Users/juniorportom/projects/uniandes/pruebas_automaticas/talleres/regression/VRT_colorPallete/cypress/screenshots/taller2/login_spec.js/')