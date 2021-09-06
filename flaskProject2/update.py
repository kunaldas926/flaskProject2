import json
import logging
import os

import boto3

from flaskProject2 import decimalencoder

dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'firstName' not in data or 'lastName' not in data or 'email' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the record.")
        return

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the todo in the database
    result = table.update_item(
        Key={
            'employeeId': event['pathParameters']['employeeId']
        },
        ExpressionAttributeNames={
            '#firstName': 'firstName',
            '#lastName': 'lastName',
            '#email': 'email',
        },
        ExpressionAttributeValues={
            ':firstName': data['firstName'],
            ':lastName': data['lastName'],
            ':email': data['email'],
        },
        UpdateExpression='SET #firstName = :firstName, '
                         'lastName = :lastName, '
                         'email = :email',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
