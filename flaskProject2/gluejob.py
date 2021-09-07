import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('glue')

glueJobName = "gluejob"


def gluejob(event):
    logger.info('## TRIGGERED BY EVENT: ')
    logger.info(event['detail'])
    response = client.start_job_run(JobName=glueJobName)
    logger.info('## STARTED GLUE JOB: ' + glueJobName)
    logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])
    return response
