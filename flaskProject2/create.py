import json
import logging
import os
import time
import uuid

import boto3

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'firstName' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'employeeId': str(uuid.uuid1()),
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'email': data['email'],
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
