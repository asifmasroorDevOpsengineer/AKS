import os
import logging
import sys, getopt
import boto3
import requests
import time
from botocore.client import Config
from botocore.exceptions import ClientError

logger = logging.getLogger('file processor')

file_path = '/usr/share/Test/input/'
rebuild_path = '/output/Managed/'

#SRC_URL = os.getenv('SOURCE_MINIO_URL', 'http://output-queue:9000')
#SRC_ACCESS_KEY = os.getenv('SOURCE_MINIO_ACCESS_KEY', 'test')
#SRC_SECRET_KEY = os.getenv('SOURCE_MINIO_SECRET_KEY', 'test@123')
#SRC_BUCKET = os.getenv('SOURCE_MINIO_BUCKET', 'input')

SRC_URL = os.getenv('TARGET_MINIO_URL', 'http://192.168.1.4:9000')
SRC_ACCESS_KEY = os.getenv('TARGET_MINIO_ACCESS_KEY', 'test')
SRC_SECRET_KEY = os.getenv('TARGET_MINIO_SECRET_KEY', 'test@123')
SRC_BUCKET = 'input'

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

SHELL_ACCESS = False

class Main():

    @staticmethod
    def log_level(level):
        logging.basicConfig(level=getattr(logging, level))

    @staticmethod
    def download_from_minio(inputfile):

        try:
            s3 = boto3.resource('s3', endpoint_url=SRC_URL, aws_access_key_id=SRC_ACCESS_KEY,
                                aws_secret_access_key=SRC_SECRET_KEY, config=Config(signature_version='s3v4'))
            logger.debug('Check if the Bucket {} exists'.format(SRC_BUCKET))
            if (s3.Bucket(SRC_BUCKET) in s3.buckets.all()) == False:
                logger.info('Bucket {} not found.'.format(SRC_BUCKET))
                return
            bucket = s3.Bucket(SRC_BUCKET)

            #for file in bucket.objects.all():
            for file in bucket.objects.filter(Prefix=inputfile):
                path, filename = os.path.split(file.key)
                obj_file = file_path + filename
                logger.info('Downloading file {}.'.format(filename))
                bucket.download_file(file.key, obj_file)
                # we only are intrested in processing the first file if it exists
                break

        except ClientError as e:
            logger.error("Cannot Connect to the Minio {}. Please Verify your credentials.".format(URL))
        except Exception as e:
            logger.error(e)

    @staticmethod
    def application(inputfile):
        endpoint = '/minio/health/ready'

        URL = SRC_URL + endpoint
        logger.debug('Checking if the Source Minio {} is avaliable.'.format(SRC_URL))
        try:
            response2 = requests.get(URL, timeout=2)
            if response2.status_code == 200:
                logger.debug('Recieved status code {} from Minio {}.'.format(response2.status_code, URL))
                Main.download_from_minio(inputfile)

            else:
                logger.error('Could not connect to the Soruce Minio {}.'.format(URL))
                exit(2)
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