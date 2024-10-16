import os
import logging
import sys, getopt
import boto3
import requests
import time
from botocore.client import Config
from botocore.exceptions import ClientError

logger = logging.getLogger('file processor')

file_path = '/usr/share/Test/output/'
rebuild_path = '/output/Managed/'

TGT_URL = os.getenv('TARGET_MINIO_URL', 'http://192.168.1.4:9000')
TGT_ACCESS_KEY = os.getenv('TARGET_MINIO_ACCESS_KEY', 'test')
TGT_SECRET_KEY = os.getenv('TARGET_MINIO_SECRET_KEY', 'test@123')
TGT_BUCKET = os.getenv('TARGET_MINIO_BUCKET', 'output')

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

class Main():

    @staticmethod
    def log_level(level):
        logging.basicConfig(level=getattr(logging, level))

    @staticmethod
    def upload_to_minio(file_path, filename):

        try:
            logger.info('Uploading file {}.'.format(filename))

            s3 = boto3.resource('s3', endpoint_url=TGT_URL, aws_access_key_id=TGT_ACCESS_KEY,
                                aws_secret_access_key=TGT_SECRET_KEY, config=Config(signature_version='s3v4'))
            logger.debug('Checking if the Bucket to upload files exists or not.')
            if (s3.Bucket(TGT_BUCKET) in s3.buckets.all()) == False:
                logger.info('Bucket not Found. Creating Bucket.')
                s3.create_bucket(Bucket=TGT_BUCKET)
            logger.debug('Uploading file to bucket {} minio {}'.format(TGT_BUCKET, TGT_URL))
            file_to_upload = file_path + filename
            s3.Bucket(TGT_BUCKET).upload_file(file_to_upload, filename)
        except ClientError as e:
            logger.error("Cannot connect to the minio {}. Please vefify the Credentials.".format(TGT_URL))
        except Exception as e:
            logger.info(e)

    @staticmethod
    def application(filename):
        endpoint = '/minio/health/ready'
        logger.debug('Checking if the Target Minio {} is avaliable.'.format(TGT_URL))
        URL = TGT_URL + endpoint
        try:
            response = requests.get(URL, timeout=2)
            if response.status_code == 200:
                logger.debug('Recieved Response code {} from {}'.format(response.status_code, URL))
                Main.upload_to_minio(file_path, filename)
            else:
                logger.error('Could Not connect to Target Minio {}.'.format(URL))
                exit(1)
        except:
            logger.error('Could not connect to Minio {}'.format(URL))

    @staticmethod
    def main(argv):
        filename = ''
        try:
            opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            print ('test.py -i <filename>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('test.py -i <filename>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                filename = arg

        Main.log_level(LOG_LEVEL)
        Main.application(filename)

if __name__ == "__main__":
    Main.main(sys.argv[1:])