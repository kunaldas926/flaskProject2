import os
import json
import logging

from flaskProject2 import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    logging.debug(event)

    # fetch todo from the database
    result = table.get_item(
        Key={
            'employeeId': event['pathParameters']['employeeId']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
